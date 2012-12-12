from __future__ import unicode_literals, print_function
import uuid

CLIENT_ID_FOR_INSTALLED_APPLICATIONS = {"installed":{"auth_uri":"https://accounts.google.com/o/oauth2/auth", "client_secret":"sdumbJRo_7MqPdTJ72ydi5zR", "token_uri":"https://accounts.google.com/o/oauth2/token", "client_email":"", "redirect_uris":["urn:ietf:wg:oauth:2.0:oob", "oob"], "client_x509_cert_url":"", "client_id":"674875767148.apps.googleusercontent.com", "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs"}}

auth_uri = CLIENT_ID_FOR_INSTALLED_APPLICATIONS["installed"]["auth_uri"]
client_id = CLIENT_ID_FOR_INSTALLED_APPLICATIONS["installed"]["client_id"]
client_secret = CLIENT_ID_FOR_INSTALLED_APPLICATIONS["installed"]["client_secret"]
auth_provider_x509_cert_url = CLIENT_ID_FOR_INSTALLED_APPLICATIONS["installed"]["auth_provider_x509_cert_url"]
token_uri = CLIENT_ID_FOR_INSTALLED_APPLICATIONS["installed"]["token_uri"]

class GoogleOAuth2Credentials(object):
    
    def __init__(self, credential_dict_given_by_google = None):
        if credential_dict_given_by_google is None:
            pass
            #TODO

SALT = b"diopioahpqu788guahoivanio"
if __name__ == "__main__":
    import hmac
    h = hmac.new(SALT)
    h.update(hex(uuid._windll_getnode()))
    print (h.hexdigest())
    #for x in CLIENT_ID_FOR_INSTALLED_APPLICATIONS["installed"].iteritems():
    #    print(x)
    import slowaes
    moo = slowaes.AESModeOfOperation()
    cleartext = "This is a test!"
    cypherkey = [143,194,34,208,145,203,230,143,177,246,97,206,145,92,255,84]
    iv = [103,35,148,239,76,213,47,118,255,222,123,176,106,134,98,92]
    mode, orig_len, ciph = moo.encrypt(cleartext, moo.modeOfOperation["CBC"],
            cypherkey, moo.aes.keySize["SIZE_128"], iv)
    print ('m=%s, ol=%s (%s), ciph=%s' % (mode, orig_len, len(cleartext), ciph))
    decr = moo.decrypt(ciph, orig_len, mode, cypherkey,
            moo.aes.keySize["SIZE_128"], iv)
    print (decr)
