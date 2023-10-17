#  Copyright (c) Huawei Technologies Co., Ltd. 2023-2023. All rights reserved.
from __future__ import unicode_literals
import json
import logging
from pangukitsappdev.agent.agent_action import AgentAction
from pangukitsappdev.agent.agent_session import AgentSession
from pangukitsappdev.api.agent.base import AbstractAgent
from pangukitsappdev.api.llms.base import LLMApi
from pangukitsappdev.api.tool.base import MARK_PLUGIN, DEFAULT_SINGLE_ARG
from pangukitsappdev.prompt.prompt_tmpl import PromptTemplates

logger = logging.getLogger(__name__)


class ReactPanguAgent(AbstractAgent):
    MARK_2 = "<unused2>"
    MARK_3 = "<unused3>"

    def __init__(self, llm: LLMApi):
        super(ReactPanguAgent, self).__init__(llm)

    def react(self, agent_session: AgentSession):
        actions = agent_session.history_action
        # 超过最大迭代次数限制，不再执行
        self.check_max_iteration(agent_session)

        # 构造React prompt
        react_tp = PromptTemplates.get("agent_react_pangu")
        actions_list = []
        for action in actions:
            action_dict = action.dict(exclude_none=True, exclude={"action_json", "action_input"})
            if action.action_json:
                action_dict["actionJson"] = action.action_json
            if action.action_input:
                action_dict["actionInput"] = action.action_input
            actions_list.append(action_dict)
        final_prompt = react_tp.format(tool_desc=self.get_tool_desc(),
                                       prompt=agent_session.query,
                                       actions=actions_list)
        # 调用llm
        answer = self.llm.ask(final_prompt).answer

        # 获取工具，例如：reserve_meeting_room|{'meetingRoom':'2303','start':'03:00','end':'08:00'}\n\n
        tool_use = self.sub_str_before(self.sub_str_between(answer, MARK_PLUGIN, self.MARK_3), self.MARK_2)
        tool_id = self.sub_str_before(tool_use, "|")
        # 未找到工具则返回
        if tool_id == "":
            action = AgentAction(thought=answer,
                                 action=self.FINAL_ACTION,
                                 action_input=answer)
            agent_session.current_action = action
            return
        tool = self.tool_map.get(tool_id)
        action = AgentAction(resp=answer,
                             thought=self.sub_str_before(answer, self.MARK_2),
                             action_json="",
                             action=tool_id)
        agent_session.current_action = action

        # 提取工具参数
        action.action_input = self.sub_str_after(tool_use, "|").replace("\'", "\"")
        if tool.input_type in [int, float, str, bool]:
            tool_input = json.loads(action.action_input)[DEFAULT_SINGLE_ARG]
        else:
            tool_input = json.loads(action.action_input)

        # 执行工具
        self.tool_execute(tool, tool_input, agent_session)
        logger.info("actions = %s", "\n".join([action.json(ensure_ascii=False) for action in actions]))
        # 执行下一迭代
        self.react(agent_session)

    def get_tool_desc(self):
        return PromptTemplates.get("agent_tool_desc_pangu").format(tools=[{"panguFunction": tool.get_pangu_function()}
                                                                          for tool in self.tool_map.values()])
