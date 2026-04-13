import os
import logging
from copy import deepcopy
from datetime import datetime
from lagent.actions import AsyncWebBrowser, WebBrowser
from lagent.agents.stream import get_plugin_prompt
from lagent.prompts import InterpreterParser, PluginParser
from lagent.utils import create_object
from . import models as llm_factory
from .mindsearch_agent import AsyncMindSearchAgent, MindSearchAgent
from .mindsearch_prompt import (
    FINAL_RESPONSE_CN,
    FINAL_RESPONSE_EN,
    GRAPH_PROMPT_CN,
    GRAPH_PROMPT_EN,
    searcher_context_template_cn,
    searcher_context_template_en,
    searcher_input_template_cn,
    searcher_input_template_en,
    searcher_system_prompt_cn,
    searcher_system_prompt_en,
)

LLM = {}

def init_agent(lang="cn",
               model_format="internlm_server",
               search_engine="BingSearch",
               use_async=False):
    mode = "async" if use_async else "sync"
    llm = LLM.get(model_format, {}).get(mode)
    if llm is None:
        llm_cfg = deepcopy(getattr(llm_factory, model_format))
        if llm_cfg is None:
            raise NotImplementedError
        if use_async:
            cls_name = (
                llm_cfg["type"].split(".")[-1] if isinstance(
                    llm_cfg["type"], str) else llm_cfg["type"].__name__)
            llm_cfg["type"] = f"lagent.llms.Async{cls_name}"
        llm = create_object(llm_
