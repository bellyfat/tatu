#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import falcon
import json
from oslo_log import log as logging
from tatu.api import models
from tatu.db.persistence import SQLAlchemySessionManager

LOG = logging.getLogger(__name__)

class RootPage(object):
    def on_get(self, req, resp):
        resp.body = json.dumps({})
        resp.status = falcon.HTTP_OK

def create_app(sa):
    LOG.info("Creating falcon API instance for authenticated API calls.")
    api = falcon.API(middleware=[models.Logger(), sa])
    api.add_route('/authorities', models.Authorities())
    api.add_route('/authorities/{auth_id}', models.Authority())
    api.add_route('/usercerts', models.UserCerts())
    api.add_route('/usercerts/{serial}', models.UserCert())
    api.add_route('/hosts', models.Hosts())
    api.add_route('/hosts/{host_id}', models.Host())
    api.add_route('/hostcerts', models.HostCerts())
    api.add_route('/hostcerts/{host_id}/{fingerprint}', models.HostCert())
    api.add_route('/hosttokens', models.Tokens())
    api.add_route('/novavendordata', models.NovaVendorData())
    api.add_route('/revokeduserkeys/{auth_id}', models.RevokedUserKeys())
    api.add_route('/pats', models.PATs())
    return api

def create_noauth_app(sa):
    LOG.info("Creating falcon API instance for unauthenticated API calls.")
    api = falcon.API(middleware=[models.Logger(), sa])
    api.add_route('/hostcerts', models.HostCerts())
    api.add_route('/revokeduserkeys/{auth_id}', models.RevokedUserKeys())
    api.add_route('/', RootPage())
    return api

def auth_factory(global_config, **settings):
    return create_app(SQLAlchemySessionManager())

def noauth_factory(global_config, **settings):
    return create_noauth_app(SQLAlchemySessionManager())
