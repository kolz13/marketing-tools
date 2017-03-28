import os
base_directory = os.getcwd()

header = '''<!DOCTYPE html>
<html lang="en">

<head>
    <link rel="icon" href="https://www.zippia.com/assets/favicon-b694b93595f7da0acb24bfb63123e1ed.ico">
    <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,300,700' rel='stylesheet' type='text/css'>
    <link rel='stylesheet' href='https://netdna.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css'>
    <link rel="stylesheet" href="https://research.zippia.com/files/application-c323b78901c98d2406b8117bdd9c4e20.css" name="css" async="" defer="">
    <link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css' async defer>
    <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Roboto:400,300,500,700' async defer>
    <link rel="stylesheet" href="https://research.zippia.com/files/kolmar.css" name="css" async="" defer="">


<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

{head}

<script>
  (function(i,s,o,g,r,a,m){{i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){{
  (i[r].q=i[r].q||[]).push(arguments)}},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  }})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-63470368-3', 'auto');
  ga('send', 'pageview');

</script>

</head>


<!--Navigation -->
    <nav class="navbar" role="navigation" style="border-bottom:1px solid #efefef;">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <div class="navbar-brand">Zippia Marketing Tools</div>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li>
                        <a href="/">Statistics</a>
                    </li>
                    <li>
                        <a href="/map-maker/">Map Maker</a>
                    </li>
                    <li>
                        <a href="/table-maker/">Table Maker</a>
                    </li>
                    <li>
                        <a href="/gallery-maker/">Gallery Maker</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>

<body><div class="container">
'''

footer = '''
<div class="row" style="margin-top:20px;border-top:1px solid #efefef;">
	<div class="col-sm-3">
		<h3>Guides</h3>
		<ul>
			<li><a href='https://docs.google.com/document/d/1t4IlB5qqS535dPMSaolgboLD6AM_xdbYrMQtGTo2sls/edit' target="blank">Style Guide</a></li>
			<li><a href='https://docs.google.com/document/d/1rAEJQXo0gg2BbtE17T7__E6s3NLyRRCd9VT_gA7ijsw/edit' target="blank">Upload To Wordpress</a></li>
			<li><a href='https://docs.google.com/document/d/1QphQDCF6BK-r9BW9Xjfo0t3ggquQlqvpBhsxdOzoIPk/edit' target="blank">Ranking Template</a></li>
		</ul>
	</div>
	<div class="col-sm-3 col-md-offset-1">
		<h3>Outreach Docs</h3>
		<ul>
			<li><a href='https://docs.google.com/spreadsheets/d/1tyNZFJ5eJu0fNs2NSKjfJ03108bsPRHjE4YDQP3EqwQ/edit#gid=0' target="blank">Email Database</a></li>
			<li><a href='https://docs.google.com/document/d/17tuWPLi-h564YAOMr_Mfkc6HytzLBdxD6-mv_qTFoZY/edit' target="blank">Past Emails</a></li>
		</ul>		
	</div>
	<div class="col-sm-3 col-md-offset-1">
		<h3>Recommended Reading</h3>
		<ul>
			<li><a href='https://priceonomics.com/the-content-marketing-handbook/' target="blank">Content Marketing Handbook</a></li>
			<li><a href='https://moz.com/beginners-guide-to-seo' target="blank">Moz - Beginners Guide To SEO</a></li>
			<li><a href='http://backlinko.com/seo-copywriting' target="blank">Backlinko - SEO Writing</a></li>
		</ul>	
	</div>
</div><!--row-->
</div><!--container-->
</body>
</html>
'''
