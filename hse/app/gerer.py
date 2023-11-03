import uuid
import random
import string

def generate_id(length=10):
    characters = string.ascii_letters + string.digits
    generated_id = ''.join(random.choice(characters) for _ in range(length))
    return generated_id









# def gerer_uid(poste):
    
#     generated_uuid = uuid.uuid4()
    
#     if poste =="jovena" :
#         resultat_uuid = 'J' + str(generated_uuid)
    
#     elif poste == "station":
#         resultat_uuid = 'S' + str(generated_uuid)
        
#     elif poste == "prestataire":
#         resultat_uuid = 'P' + str(generated_uuid)
        
#     else :
#         resultat_uuid = 'T' + str(generated_uuid)
        
#     return uuid.UUID(resultat_uuid)