import openai
import backoff
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
    retry_if_not_exception_type,
)
def openai_calls_variables(timeout, n_retries):
    return timeout, n_retries

@retry(wait=wait_random_exponential(min=1, max=openai_calls_variables[0]), stop=stop_after_attempt(openai_calls_variables[1]), retry=retry_if_not_exception_type(openai.InvalidRequestError))
def create_chat_completion(model, messages, max_tokens, temperature, number_of_prompts, logit_bias=None, functions=None, function_call=None):
    
    try:
        if (logit_bias==None and functions==None):

            respond = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                n = number_of_prompts,
                temperature=temperature,
                request_timeout=60,
            )

        elif functions!=None:
                
            respond = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                n = number_of_prompts,
                temperature=temperature,
                functions=functions,
                function_call=function_call,
                request_timeout=60,
            )

        else:

            respond = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                n = number_of_prompts,
                temperature=temperature,
                logit_bias=logit_bias,
                request_timeout=60,
            )
    
    except openai.error.OpenAIError as e:
        print(f"Error in request: {e}")
        raise
            
    return respond

@retry(wait=wait_random_exponential(min=1, max=openai_calls_variables[0]), stop=stop_after_attempt(openai_calls_variables[1]), retry=retry_if_not_exception_type(openai.InvalidRequestError))
def create_embedding(model, input):

    try:
        embedding = openai.Embedding.create(
            model=model,
            input=input
        )

    except openai.error.OpenAIError as e:
        print(f"Error in request: {e}")
        raise

    return embedding