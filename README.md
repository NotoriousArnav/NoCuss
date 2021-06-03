# NoCuss
A Application that Tracks, how often you Cuss in your WhatsApp Chats! Active Development

<h1>How doees it Do so?</h1>
It uses Natural Language Processing Toolkit, nltk and then Processes the Data and Gives the Result<br>
The Processing Includes:<br>
<ul>
  <li>Removal of Stopwords (English Only)</li>
  <li>Tokenization of Words</li>
  <li>Making a FreqDist Table of it</li>
  <li>Calculating the average, and then Juding you on that basis</li>
</ul>
<h1>How to use</h1>
<ul>
  <li><h3>Jupyter Notebook</h3></li>
  Make your Own data.txt file and Run all the cells,the output should be correct!
  <li><h3>Script</h3></li>
  Same as JupyterNotebook
</ul>
<h2>Making own data.txt</h2>
It is not mandatory to use only WhatsApp Chats, but This Repo is Only testd with WhatsApp Chats!<br>
To make your own WhatsApp Data,<br>
<pre>
<code>
cat <b>$WhatsappchatFile</b> | grep '$YourWhatsAppName' >data.txt
</code>
</pre>
