 .. Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

 ..   http://www.apache.org/licenses/LICENSE-2.0

 .. Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.

Integration
===========

Airflow has a mechanism that allows you to expand its functionality and integrate with other systems.

* :doc:`API Authentication backends </security/api>`
* :doc:`Email backends </howto/email-config>`
* :doc:`Executor </core-concepts/executor/index>`
* :doc:`Kerberos </security/kerberos>`
* :doc:`Logging </administration-and-deployment/logging-monitoring/logging-tasks>`
* :doc:`Metrics (statsd) </administration-and-deployment/logging-monitoring/metrics>`
* :doc:`Operators and hooks </operators-and-hooks-ref>`
* :doc:`Plugins </administration-and-deployment/plugins>`
* :doc:`Listeners </administration-and-deployment/listeners>`
* :doc:`Secrets backends </security/secrets/secrets-backend/index>`
* :doc:`Web UI Authentication backends </security/api>`
* :doc:`Serialization </authoring-and-scheduling/serializers>`

It also has integration with :doc:`Sentry </administration-and-deployment/logging-monitoring/errors>` service for error tracking. Other applications can also integrate using
the :doc:`REST API <stable-rest-api-ref>`.
