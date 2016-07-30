import hashlib
import random
from alchemysite import settings
from django.core.urlresolvers import reverse

def getActivationEmailText(user):
    hasher = hashlib.sha256((settings.SECRET_KEY + user.email).encode())
    activationUrl = settings.DOMAIN + reverse('game:activation', args=(hasher.hexdigest(),))
    emailText = """<p>Ваш email был указан при регистрации на свйте {domain}.</p>
                    <p>Для подтверждения регистрации перейдите по <a href="{activationUrl}">ссылке</a> </p>
                    <p>Ссылка действительна в течении 1 дня. Если вы не знаете о чем идет речь, просто проигнорируйте это письмо</p>"""
    return hasher.hexdigest(), emailText.format(domain=settings.DOMAIN, activationUrl=activationUrl)