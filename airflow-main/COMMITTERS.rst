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

Committers and PMC members
==========================

Before reading this document, you should be familiar with `Contributors' guide <contributing-docs/README.rst>`__.
This document assumes that you are a bit familiar how Airflow's community work, but you would like to learn more
about the rules by which we add new members.

**The outline for this document in GitHub is available at top-right corner button (with 3-dots and 3 lines).**

Committers vs. Maintainers
--------------------------

Often you can hear two different terms about people who have write access to the Airflow repository -
"committers" and "maintainers". This is because those two terms are used in different contexts.

* "Maintainers" is term used in GitHub documentation and configuration and is a generic term referring to
  people who have write access to the repository. They can merge PRs, push to the repository, etc.
* "Committers" is a term used in Apache Software Foundation (ASF) and is a term referring to people who have
  write access to the code repository and has a signed
  `Contributor License Agreement (CLA) <https://www.apache.org/licenses/#clas>`_ on file.  They have an
  apache.org mail address. This is an official `role <https://www.apache.org/foundation/how-it-works/#roles>`_
  defined and governed by the Apache Software Foundation.

For all practical purposes, both terms are interchangeable because the Apache Software Foundation rule is
the only Committers can have write access to the repositories managed by the PMC (Project Management Committee)
and that all Committers get write access to the repository.

You will see both terms used in different documentation, therefore our goal is not to use one of the terms
only - it is unavoidable to see both terms anyway. As a rule, we are using "committer" term in the context
of the official rules concerning Apache Software Foundation and "maintainer" term in the context where
technical GitHub access and permissions to the project are important.

Guidelines to become an Airflow Committer
------------------------------------------

Committers are community members who have write access to the project's
repositories, i.e., they can modify the code, documentation, and website by themselves and also
accept other contributions. There is no strict protocol for becoming a committer. Candidates for new
committers are typically people that are active contributors and community members.

Some people might be active in several of those areas and while they might have not enough 'achievements' in any
single one of those, their combined contributions in several areas all count.

As a community, we appreciate contributions to the Airflow codebase, but we also place equal value
on those who help Airflow by improving the community in some way. It is entirely possible to become
a committer (and eventually a PMC member) without ever having to change a single line of code.


Prerequisites
^^^^^^^^^^^^^^

General prerequisites that we look for in all candidates:

1.  Consistent contribution over last few months
2.  Visibility on discussions on the dev mailing list, Slack channels or GitHub issues/discussions
3.  Contributions to community health and project's sustainability for the long-term
4.  Understands contributor/committer guidelines: `Contributors' Guide <contributing-docs/README.rst>`__


Code contribution
^^^^^^^^^^^^^^^^^^

1.  Makes high-quality commits (especially commit messages), and assess the impact of the changes, including
    upgrade paths or deprecation policies
2.  Testing Release Candidates to help the release cycle
3.  Proposed and led to completion Airflow Improvement Proposal(s)
4.  Demonstrates an understanding of one of the following areas or has displayed a holistic understanding
    of a particular part and made contributions towards a more strategic goal

    - Airflow Core
    - API
    - Docker Image
    - Helm Chart
    - Dev Tools (Breeze / CI)
    - Certain Providers

5.  Has made a significant improvement or added an integration with services/technologies important to the Airflow
    Ecosystem

6.  Actively participated in the security process, as a member of security team, discussing, assessing and
    fixing security issues.


Community contributions
^^^^^^^^^^^^^^^^^^^^^^^^

1.  Actively participates in `triaging issues <ISSUE_TRIAGE_PROCESS.rst>`_ showing their understanding
    of various areas of Airflow and willingness to help other community members.
2.  Improves documentation of Airflow in significant way
3.  Leads/implements changes and improvements introduction in the "community" processes and tools
4.  Actively spreads the word about Airflow, for example organising Airflow summit, workshops for
    community members, giving and recording talks, writing blogs
5.  Reporting bugs with detailed reproduction steps


Committer Responsibilities
^^^^^^^^^^^^^^^^^^^^^^^^^^

Committers are more than contributors. While it's important for committers to maintain standing by
committing code, their key role is to build and foster a healthy and active community.
This means that committers should:

* Review PRs in a timely and reliable fashion
* They should also help to actively whittle down the PR backlog
* Answer questions (i.e. on the dev list, in PRs, in GitHub Issues, slack, etc...)
* Take on core changes/bugs/feature requests
* Some changes are important enough that a committer needs to ensure it gets done. This is especially
  the case if no one from the community is taking it on.
* Improve processes and tooling
* Refactoring code


Guidelines for promoting Committers to Airflow PMC
---------------------------------------------------

To become a PMC member the committers should meet all **general prerequisites**.
Apart from that the person should demonstrate distinct **community involvement** or **code contributions**.

Guidelines from ASF are listed at
`ASF: New Candidates for Committership <http://community.apache.org/newcommitter.html#guidelines-for-assessing-new-candidates-for-committership>`__.

Prerequisites
^^^^^^^^^^^^^^

* Has been a committer for at least 3 months
* Is still active community member (Visible on mailing list or reviewing PRs at the minimum)

Community involvement
^^^^^^^^^^^^^^^^^^^^^^

* Visibility on discussions on the dev mailing list
* Spreading the word for "Airflow" either:

  * Talks at meetups, conferences, etc
  * Creating content like videos, blogs, etc

* Growing the community:

  * Mentors new members/contributors
  * Answers users/contributors via GitHub issues, dev list or slack

Code contribution
^^^^^^^^^^^^^^^^^^

* Consistent voting on RCs for at least past 3 releases lifecycles
* Engagement in Airflow Improvements Proposals either:

  * Has been actively voting on AIPs
  * Has been proposing and leading their implementation

* Actively involved in code contributions:

  * Code reviews
  * Merging pull requests
  * Fixing bugs and implementing improvements
  * Actively participating in the security process and significantly contributing to overall security of
    Airflow


Only a current PMC member can nominate a current committer to be part of PMC.

If the vote fails or PMC members needs more evidence, then one of the PMC Member (who is not the Proposer)
can become the Mentor and guide the proposed candidates on how they can become a PMC member.

1.  Candidate Proposer

    This is the person who launches the DISCUSS thread & makes the case for a PMC member promotion

2.  Candidate Mentor

    If the committee does not have enough information, requires more time, or requires more evidence of
    candidate's eligibility, a mentor, who is not the proposer, is selected to help mentor the candidate
    The mentor should try to remain impartial -- their goal is to provide the missing evidence and to
    try to coach/mentor the candidate to success.

    In order to re-raise a candidate vote, both Proposer and Mentor must be in favor. Again,
    the mentor must try to remain impartial and cannot be the Proposer.


Inactive Committers
-------------------
If you know you are not going to be able to contribute for a long time
(for instance, due to a change of job or circumstances), you should inform the PMC and we will mark you
as "inactive". Inactive committers will be removed from the "roster" on ASF and will no longer have the power
of being a Committer (especially write access to the repos). As merit earned never expires, once you
become active again you can simply email the PMC and ask to be reinstated.

The PMC also can mark committers as inactive after they have not been involved in the community for
more than 12 months.

New Committer Onboarding Steps
------------------------------

To be able to merge PRs, committers have to integrate their GitHub ID with Apache systems. To do that follow steps:

1.  Verify you have a GitHub ID `enabled with 2FA <https://help.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/>`__.
2.  Merge your Apache and GitHub accounts using `GitBox (Apache Account Linking utility) <https://gitbox.apache.org/setup/>`__. This also asks you to link your
    GitHub ID to your Apache account. You should see 5 green checks in GitBox.
3.  Wait at least 30  minutes for an email inviting you to Apache GitHub Organization and accept invitation.
4.  After accepting the GitHub Invitation verify that you are a member of the `Airflow committers team on GitHub <https://github.com/orgs/apache/teams/airflow-committers>`__.
5.  Ask in ``#internal-airflow-ci-cd`` channel to be `configured in self-hosted runners <https://github.com/apache/airflow-ci-infra/blob/main/scripts/list_committers>`_
    by the CI team. Wait for confirmation that this is done and some helpful tips from the CI team (Temporarily disabled)
6.  After confirming that step 5 is done, open a PR to include your GitHub ID in:

    * ``dev/breeze/src/airflow_breeze/global_constants.py`` (COMMITTERS variable)
    * name and GitHub ID in `project.rst <https://github.com/apache/airflow/blob/main/airflow-core/docs/project.rst>`__.
    * If you had been a collaborator role before getting committer, remove your GitHub ID from ``.asf.yaml``.
7.  Raise a PR to `airflow-site <https://github.com/apache/airflow-site>`_ repository with the following additions:

    * List your name(s) in the `committers list <https://github.com/apache/airflow-site/blob/main/landing-pages/site/data/committers.json>`__.
    * Post an entry in `Announcements <https://github.com/apache/airflow-site/blob/main/landing-pages/site/content/en/announcements/_index.md>`__.

    **A kind request**: If there are other committers who joined around the same time, please create a unified PR for all of you together.
