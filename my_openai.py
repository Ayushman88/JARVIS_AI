# import os
# import openai
# from apikey import apikey
#
# openai.api_key = apikey
#
# response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt="Write me a nursery poem",
#     temperature=1,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
# )
#
# print(response)
# '''
# {
#   "id": "cmpl-7dImlRU0gRLhc3CKInX0MgfDnPThi",
#   "object": "text_completion",
#   "created": 1689601359,
#   "model": "text-davinci-003",
#   "choices": [
#     {
#       "text": "\n\nTwinkle twinkle itty bitty star, \nHow I wonder what you are. \nUp above they sky so high, \nLike a diamond in the sky.\n\nTwinkle twinkle little one,\nIn your crib you will have lots of fun.\nGently cradle in your dreams,\nLet the cuckoo's tune sing you to sleep.\n\nTwinkle twinkle little star,\nSo gentle you'll never wander far.\nSoftly shine your tender light,\nWrap the world in calm and delight.",
#       "index": 0,
#       "logprobs": null,
#       "finish_reason": "stop"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 5,
#     "completion_tokens": 116,
#     "total_tokens": 121
#   }
# }
# '''