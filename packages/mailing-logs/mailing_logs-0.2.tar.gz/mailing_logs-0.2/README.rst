mailing_logs
============

easy logs with package

How to use
==========

.. code:: python

   from mailing_logs import MailingLogs

   log = MailingLogs(tg_token="YOUR_TG_TOKEN")

   for profile in profiles:
       message = send_foo(...)
       log.append(profile.chat_id, message.message_id)  # chat_id, message_id

   log.send_to_tg(YOUR_ACCOUNT_ID)  # send a logs file to your telegram account