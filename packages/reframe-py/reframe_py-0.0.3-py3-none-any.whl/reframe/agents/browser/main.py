#!/usr/bin/env python

__authors__ = ["Peter W. Njenga"]
__copyright__ = "Copyright © 2023 ReframeAI, Inc."

# Standard Libraries

# External Libraries
from loguru import logger

# Internal Libraries
from reframe.lib.models.llms.main import OpenAI
from reframe.lib.core.main import SingleActionChatAgent

# Global Variables
llm = OpenAI()

browser_agent = SingleActionChatAgent(
    name="browser",
    invoke_commands=["browse", "visit", "open"],
    tool_list=[{
        "display_name": "Browser",
        "name": "browser",
        "id": "browser",
        "output": "web_page_content"
    }],
    chat_template = [
        {"role": "system", "content": "Given the following content. Return the information asked without generating "
                                      "superfluous text. Answer with as few words as possible."},
        {"role": "user", "content": "{{web_page_content}}"},
        {"role": "assistant", "content": "Thanks. I have understood the context. Please provide the prompt"},
        {"role": "user", "content": "{{llm_prompt}}"}
    ],
    llm=llm
)

if __name__ == "__main__":
    logger.info(f"🏁 Starting Browser agent")
    browser_agent.run()