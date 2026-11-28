SMS spam messages (sms_spam.csv)
================================

Used in: DSC 210 Homework 8 (Module 12, text as data). Revised 2026-11-28 with a stricter keyword list.

Source
------
SMS Spam Collection v.1: 5,572 English text messages, each labeled "ham" (ordinary) or "spam".
T. A. Almeida, J. M. Gomez Hidalgo, and A. Yamakami (2011), "Contributions to the Study of
SMS Spam Filtering: New Collection and Results," Proceedings of the 11th ACM Symposium on
Document Engineering (DocEng '11).
Distributed through the UCI Machine Learning Repository: https://archive.ics.uci.edu/dataset/228/sms+spam+collection
Copy used to build this file: https://github.com/justmarkham/pycon-2016-tutorial (data/sms.tsv), downloaded 2026-11-28.

Changes made for DSC 210
------------------------
358 messages (254 ham, 104 spam) were removed because they contain profanity, sexual content,
or drug references, matched with a keyword list kept by the instructor. 5,214 messages remain
(4,571 ham, 643 spam; 12.3% spam). Nothing else was changed: message text, duplicates, and the dataset's own
placeholders (&lt;#&gt;, &lt;DECIMAL&gt;, &lt;URL&gt;, &lt;TIME&gt;) are as in the source.

Columns
-------
label    "ham" or "spam"
message  the text of the message, as typed

Notes
-----
- 389 messages are exact copies of an earlier message (303 ham, 86 spam).
- Keyword filtering is imperfect; a few remaining spam messages advertise dating or chat services in mild terms.
