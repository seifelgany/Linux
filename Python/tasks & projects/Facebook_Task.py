import requests
#  
page_id_1 = 120225371063440
facebook_access_token_1 = 'EAAJZAyJmeP3UBAEvm9FOl28ZA0eEZBQLtZA1nrpl9Mcy05IR4iSPqHJx5YUvcGsl0eN2hNZAP53TR6hKtdzMnrTWZA2nZCoC5ZAZC25dWfxjn1wooO9zeZCWAmOxCaaNp1u4h4m2WscXy31PCZB3MuL5RBEGJdaD9IRhCjHCjFYkW8fwQY03T07WuIzCiZA1GiQwltUCw30GinrTUs55q3ZAexVHI'
msg = 'Python task to post in facebook with python script'
post_url = 'https://graph.facebook.com/{}/feed'.format(page_id_1)
payload = {
'message': msg,
'access_token': facebook_access_token_1
}
r = requests.post(post_url, data=payload)
print(r.text)