from promptmanager.runtime.flow import PMNodeOutput
import logging

logger = logging.getLogger('pm_log')

OPENAI_API_KEY = 'OPENAI_API_KEY'


class JsonAgent:
    def __init__(self, openai_api_key, model):
        self.openai_api_key = openai_api_key
        self.model = model

    def exec(self, file_path, query_text) -> str:
        import os
        from promptmanager.script.base.agents import create_json_agent
        from promptmanager.script.base.agents.agent_toolkits import JsonToolkit

        from promptmanager.script.base.tools.json.tool import JsonSpec

        if file_path.endswith('.yml'):
            import yaml
            with open(file_path, encoding='utf-8') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
        else:
            import json
            with open(file_path, encoding='utf-8') as f:
                content = f.read()
                data = json.loads(content)

        json_spec = JsonSpec(dict_=data, max_value_length=4000)
        json_toolkit = JsonToolkit(spec=json_spec)

        os.environ[OPENAI_API_KEY] = self.openai_api_key

        # json_agent_executor = create_json_agent(
        #     llm=OpenAI(temperature=0), toolkit=json_toolkit, verbose=True
        # )
        json_agent_executor = create_json_agent(
            llm=self.model, toolkit=json_toolkit, verbose=True
        )

        results = json_agent_executor.run(query_text)

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

    file_path = params['script']['csv_path']['value']
    model = params['script']['model']['value']
    openai_api_key = params['script']['openai_api_key']['value']

    query_text = inputs['query_text']['value']

    json_agent = JsonAgent(openai_api_key, model)
    result = json_agent.exec(file_path=file_path, query_text=query_text)

    output = PMNodeOutput()
    for output_name in outputs.keys():
        output.add_output(output_name, result)

    return output
