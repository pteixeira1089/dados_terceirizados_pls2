# dados_terceirizados_pls2
This set of scripts is made to extract outsource employees data from html files saved from public STJ webpages.

## Integrity tests
One of the team members downloaded all the html files to a directory (dados_html). 
Thus, before extracting the data from all files and consolidating them in a csv file, it's important to perform tests on the integrity of the downloades html files, as follows:
* Each file contains a report of a given month, in a given period of time (2014, january to a given date [ideal: actual date])
* The file name has to reflect the date of the report it contains. e.g: the html file that contains the march-2014 report has to be named '2014-03-01.html' ('yyyy-mm-dd' format);
* For each given date in the analysed period there must be one corresponding file (i.e. it's important to check if all the files expected were actually saved in the directory);
* There must be a general check-out for repeated reports saved with different names. e.g. in the case the report of october-2020 was saved twice, once with the expected name (2020-10-01.html) and another with a wrong name (2020-11-01.html, for example), the test has to be able to identify and report this error. Notice that this test complements the first and second ones - if there are errors in this test, there will be errors in ther first one, too, and if there is an error on the second test, this test will also raise a notification;
* The inconsistences has to be outputed in a csv file
