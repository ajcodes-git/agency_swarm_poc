# AGENCY_SWARM POC

## Getting started

run agency.py as the entry point if you have an openAI key.

if not...

Focus your attention on agency_with_groq.py.

agency.py with openAPI gives waayyy better results.

Thanks :)


## Things To Know About OpenAI Assistant API:
    - It is very stable with agency_swarm as it is the default assistant api used by the framework.
    - OpenAI assistant api supports File operations, Code intepretation, and function calling.
    - function calling is what agency_swarm leverages to running the set of tools provided when creating an agent.

## Things To Know About Astra Assistant API:
    - One of the alternatives for OpenAI Assistant API.
    - 40 out of the 57 OpenAI API endpoints are implemented making it a good substitute for OpenAI assistant api (outdated fact).
    - Uses Astra DB Serverless database as its vector store.
    - compatible with completion models with hundreds of LLMs, including Anthropic, Gemini, Mistral, Groq, LLama, and Cohere.
    - Astra Assistant API claims to be the best and the easiest option for running Open Source models

## Limitations of integrating agency_swarm with open-source-models
    - Function calling is not supported by most open-source models: This limitation prevents the agent from communicating with other agents in the agency. So, it must be positioned at the end of the agency chart and cannot utilize any tools.
    - RAG is typically limited: Most open-source assistants API implementations have restricted Retrieval-Augmented Generation capabilities. It is recommended to develop a custom tool with your own vector database (Don't worry. This does not apply to Astra Assistant API).
    - CodeInterpreter is not supported: The Code Interpreter feature is still under development for all open-source assistants API implementations (Something to worry about!).
    
    
## links
    - https://vrsen.github.io/agency-swarm/advanced-usage/open-source-models/
    - https://docs.datastax.com/en/astra-db-serverless/tutorials/astra-assistants-api.html
    - https://www.datastax.com/blog/getting-started-with-the-astra-assistants-api