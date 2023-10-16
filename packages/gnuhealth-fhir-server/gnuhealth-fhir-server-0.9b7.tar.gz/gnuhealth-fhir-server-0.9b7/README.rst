.. image:: https://www.gnuhealth.org/downloads/artwork/logos/gnu-health-HL7-FHIR.png

THE GNU HEALTH FHIR SERVER
==========================

The GNU Health Fast Healthcare Interoperability Resources (FHIR) server allows
to query different resources from a running GNU Health HMIS node, returning
HL7 FHIR messages.

History
-------
In March 2014 I started the initial alpha FHIR project for Python with the idea
to be used in GNUHealth HMIS (server and client) and other EMRs.
(https://pypi.org/project/fhir)

Soon after, our colleague Dr. Chris Zimmerman joined the project and
did an phenomenal job continuing and leading for years the development 
of HL7 FHIR server for GNUHealth. 

For several years, the FHIR development was part of the GNU Health HMIS
"backend". Although at the beginning was convenient, we felt that the 
GNU Health FHIR component deserved its own reporitory. In 2020, we created
the health-fhir-server mercurial repository in GNU Savannah. This allows
to have a team dedicated to the FHIR resources.

In 2020, we created the GNU Health FHIR server package at Pypi 
(https://pypi.org/project/gnuhealth-fhir-server)

The GNU Health FHIR server is work in progress. We are happy to work 
with the HL7 FHIR community, adding new resources and functionality.

The development, as other GNU Health components, is at GNU Savannah.


Installation
------------

The GNU Health FHIR server is pip installable

The server requires Flask and a few of its addons. And, of course, a working
GNU Health HMIS instance. 

  $ pip3 install --upgrade --user gnuhealth-fhir-server


Configuration
-------------

The server ships with a simple production config file (server/config.py). However, 
it needs to be edited.::

 TRYTON_DATABASE = ''    # GNU Health database
 SERVER_NAME = ''        # Domain name of the server (e.g., fhir.example.com)
 SECRET_KEY = ''         # Set this value to a long and random string


Security
--------

Use TLS. Sensitive medical information must be protected and confidential.

By default, all FHIR endpoints except the Conformance statement require user 
authentication. The user authentication and access follows Tryton's model, 
respecting model and field access rights.

The same credentials used to sign into GNU Health are used to access the 
FHIR REST server.


Running the server
------------------

For development, you can just run:

python ./gnuhealth_fhir_server.py 

For production environments, you should run it from a WSGI container,
such as gunicorn, uWSGI or Tornado.

* uwsgi server_uwsgi.ini 

You can change the port (default 8020) and sockets in the server_uwsgi.ini

Current resources / endpoints
-----------------------------

Currently the following resources are implemented (read-only):

The FHIR standard defines a REST API, a set of interactions with each resource. Each resource handles different types of information. Currently, the GNU Health FHIR server supports 12 resources:

*    **Conformance**: Describes the server's FHIR capabilities.
*    **Patient**: Patient information, like email, address, SSN, etc.
*    **DiagnosticReport**: Completed lab tests, but not the data
*    **Observation**: Lab data, like Uric Acid values
*    **Practitioner**: Health professionals and their information
*    **Procedure**: Surgeries/operations
*    **Condition**: Diseases/diagnoses
*    **FamilyHistory**: Family histories of patients
*    **Medication**: Medications (not prescriptions!)
*    **MedicationStatement**: Medications taken by a patient
*    **Immunization**: Immunizations
*    **Organization**: Institutions, departments, companies, etc.

Each resource has its own endpoint. For example, the Patient endpoint is found at /Patient, the DiagnosticReport endpoint at /DiagnosticReport, and so on. The only exception to this naming schema is the Conformance endpoint which is found at / and /metadata. 

Querying the GNU Health FHIR Server
-----------------------------------

If we enter the resource name as the endpoint, GNU Health will bring back
all the results.

For instance:
https://federation.gnuhealth.org:8700/Patient

Will retrieve the patients in the current database.

To search a resource, simply add arguments to the endpoint to refine the search. For example, **/Patient?name=ana** will return all the patients with Ana in their name


The *log* file will be stored at the user's home directory, with the name
"fhir_server.log". You can also add the corresponging log when running the server behind uwsgi.


Technology
----------
The GNU Health HMIS FHIR server is built on Flask technology 
(http://flask.pocoo.org/) .

More information about Flask and its addons used in GNU Health FHIR server:

- `Flask <https://flask.pocoo.org/>`_
- `Flask-Login <https://flask-login.readthedocs.org/en/latest/>`_
- `Flask-Tryton <https://pypi.org/project/flask-tryton/>`_
- `Flask-Restful <http://flask-restful.readthedocs.org/en/latest/quickstart.html>`_
- `Flask-WTF <https://flask-wtf.readthedocs.org/en/latest/>`_


Development
-----------
The development of GNU Health is on GNU Savannah, using the Mercurial repository.

Tasks, bugs and mailing lists will be on health-dev@gnu.org , for development.

General discussion is done at health@gnu.org mailing list.


Homepage
--------
https://www.gnuhealth.org


Documentation
-------------
The GNU Health FHIR server documentation will be at the corresponding
chapter in the GNU Health Wikibook

https://en.wikibooks.org/wiki/GNU_Health


Support GNU Health
-------------------

GNU Health is a project of GNU Solidario. GNU Solidario is an Non-profit
Non-goverment-Organization (NGO) that works globally, focused on Social Medicine.

Health and education are the basis for the development and dignity of societies.

You can also **donate** to our project via :

https://www.gnuhealth.org/donate/

In addition, you can show your long time commitment to GNU Health by
**becoming a member** of GNU Solidario, so together we can further
deliver Freedom and Equity in Healthcare around the World.

https://my.gnusolidario.org/join-us/

GNU Solidario hosts IWEEE and GnuHealthCon:

The International Workshop on e-Health in Emerging Economies- a good way to
support GNU Solidario and to get the latest on e-Health is to assist
to the conferences.

https://www.gnuhealthcon.org/


Need help to implement GNU Health ?
-----------------------------------

We are committed to do our best in helping out projects that can improve
the health of your country or region. We want the project to be a success,
and since our resources are limited, we need to work together to make a great
and sustainable project.

In order to be elegible, we need the following information from you,
your NGO or government:

* An introduction of the current needs
* The project will only use Libre software technology
* There will be a local designated person that will be in charge of  the project 
  and the know-how transfer to the rest of the community.This person must be 
  committed to be from the beginning of the project until two years after its
  completion.
* There must be a commitment of knowledge transfer to the rest of the team.

We will do our best to help you out with the implementation and training
for the local team, to build local capacity and make your project sustainable.

Please contect us and we'll back to you as soon as possible::

 Thank you !
 Dr. Luis Falcón, MD, MSc
 Author and project leader
 falcon@gnuhealth.org


Email
-----
info@gnuhealth.org

Twitter: @gnuhealth

License
--------

GNU Health, the Libre Digital Health ecosystem, is licensed under GPL v3+::

 Copyright (C) 2008-2023 Luis Falcon <falcon@gnuhealth.org>
 Copyright (C) 2011-2023 GNU Solidario <health@gnusolidario.org>

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.


