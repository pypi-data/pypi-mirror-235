from promptmanager.runtime.flow import PMNodeOutput
import logging

logger = logging.getLogger('pm_log')

OPENAI_API_KEY = 'OPENAI_API_KEY'


class CsvAgent:
    def __init__(self, model, openai_api_key):
        self.model = model
        self.openai_api_key = openai_api_key

    def exec(self, csv_path, query_text) -> str:
        import os
        # from promptmanager.script.base.llms import OpenAI
        # from promptmanager.script.base.chat_models import ChatOpenAI
        from promptmanager.script.base.agents.agent_types import AgentType
        from promptmanager.script.base.agents import create_csv_agent

        os.environ[OPENAI_API_KEY] = self.open_api_key

        agent = create_csv_agent(
            self.model,
            csv_path,
            verbose=True,
            agent_type=AgentType.OPENAI_FUNCTIONS,
        )

        # agent = create_csv_agent(
        #     ChatOpenAI(temperature=0, model=model),
        #     csv_path,
        #     verbose=True,
        #     agent_type=AgentType.OPENAI_FUNCTIONS,
        # )

        results = agent.run(query_text)

        logger.info(results)

        return results


def run(params: dict = None, inputs: dict = None, outputs=None) -> PMNodeOutput:
    logger.info("Welcome to Use Csv Agent!")
    logger.info("This is params info:")
    logger.info(params)
    logger.info("This is inputs info:")
    logger.info(inputs)
    logger.info("This is outputs info:")
    logger.info(outputs)

    csv_path = params['script']['csv_path']['value']
    model = params['script']['model']['value']
    openai_api_key = params['script']['openai_api_key']['value']

    query_text = inputs['query_text']['value']

    csv_agent = CsvAgent(model=model, openai_api_key=openai_api_key)
    result = csv_agent.exec(csv_path=csv_path, query_text=query_text)

    output = PMNodeOutput()
    for output_name in outputs.keys():
        output.add_output(output_name, result)

    return output
