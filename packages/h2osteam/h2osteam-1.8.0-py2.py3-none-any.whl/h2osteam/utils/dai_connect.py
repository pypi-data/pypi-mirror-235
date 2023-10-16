import os
import sys
import hashlib
import importlib
import tempfile
from . import LooseVersion


def dai_instance_connect(api, id, use_h2oai_client=False, use_own_client=False):
    if sys.version_info < (3, 6):
        raise Exception("Driverless AI Python client only supports Python 3.6 and above")

    if use_own_client is True and use_h2oai_client is True:
        raise Exception("Use either use_h2oai_client=True or use_own_client=True, not both.")

    instance = api.get_driverless_instance_by_id(id)

    if instance['status'] != "running":
        raise Exception("Cannot connect to Driverless AI instance. Instance in in %s state." % instance['status'])

    version = instance['version']

    if use_h2oai_client is True:
        h2oai = importlib.import_module("h2oai_client")
        return h2oai.Client('https://%s:%s/proxy/driverless/%d' % (api.host, api.port, id),
                            username=instance['created_by'],
                            password=instance['password'])

    if use_own_client is True:
        h2oai = importlib.import_module("driverlessai")
        return h2oai.Client('https://%s:%s/proxy/driverless/%d' % (api.host, api.port, id),
                            username=instance['created_by'],
                            password=instance['password'])

    whl_file = os.path.join(tempfile.gettempdir(), "steam", "driverlessai.whl")
    os.makedirs(os.path.dirname(whl_file), exist_ok=True)
    open(whl_file, 'a').close()
    hash = hashlib.md5(open(whl_file, 'rb').read()).hexdigest()

    api.download('/download/driverless/client/%s' % hash, whl_file)

    sys.path.insert(0, whl_file)
    driverlessai = importlib.import_module("driverlessai")

    if LooseVersion(version) > LooseVersion(driverlessai.__version__):
        raise Exception("This version of Driverless AI is not supported by the current driverlessai client. "
                        "Contact your Steam administrator to upload the required driverlessai client.")

    token_provider = api.get_oidc_token_provider()

    if token_provider['enabled']:
        return driverlessai.Client('https://%s:%s/proxy/driverless/%d' % (api.host, api.port, id),
                                   verify=api.requests_verify(),
                                   token_provider=driverlessai.token_providers.OAuth2TokenProvider(
                                       refresh_token=token_provider['refresh_token'],
                                       client_id=token_provider['client_id'],
                                       client_secret=token_provider['client_secret'],
                                       token_endpoint_url=token_provider['token_endpoint_url'],
                                       token_introspection_url=token_provider['token_introspection_url']
                                   ).ensure_fresh_token)

    return driverlessai.Client('https://%s:%s/proxy/driverless/%d' % (api.host, api.port, id),
                               username=instance['created_by'],
                               password=instance['password'],
                               verify=api.requests_verify())