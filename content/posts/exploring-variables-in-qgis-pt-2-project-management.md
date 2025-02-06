---
source: "blog"
title: "Exploring variables in QGIS pt 2: project management"
date: "2015-12-03T07:37:06+0000"
link: "https://nyalldawson.net/2015/12/exploring-variables-in-qgis-pt-2-project-management/"
draft: "false"
showcase: "planet"
subscribers: ["nyalldawson_net"]
author: "nyalldawson.net"
tags: ["qgis", "2.12", "geospatial", "osgeo", "qgis"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>Following on from <a href="http://nyalldawson.net/2015/12/exploring-variables-in-qgis-2-12-part-1/">part 1</a> in which I introduced how variables can be used in map composers, I&#8217;d like to now explore how using variables can make it easier to manage your QGIS projects. As a quick refresher, variables are a new feature in QGIS 2.12 which allow you to create preset values for use anywhere you can use an expression in QGIS.</p>
<p>Let&#8217;s imagine a typical map project. You load up QGIS, throw a bunch of layers on your map, and then get stuck into styling and labelling them &#8216;just right&#8217;. Over time the project gets more and more complex, with a stack of layers all styled using different rendering and labelling rules. You keep tweaking settings until you&#8217;re almost happy with the result, but eventually realise that you made the wrong choice of font for the labelling and now need to go through all your layers and labelling rules and update each in turn to the new typeface. Ouch.</p>
<p>Variables to the rescue! As you may recall from <a href="http://nyalldawson.net/2015/12/exploring-variables-in-qgis-2-12-part-1/">part 1</a>, you can reuse variables anywhere in QGIS where you can enter an expression. This includes using them for data defined overrides in symbology and labelling. So, lets imagine that way back at the beginning of our project we created a project level variable called <em>@main_label_font:</em></p>
<div class="wp-caption aligncenter" id="attachment_656" style="width: 821px;"><a href="http://nyalldawson.net/wp-content/uploads/2015/12/label_font.png"><img alt="Creating a variable for label font" class="wp-image-656 size-full" height="512" src="http://nyalldawson.net/wp-content/uploads/2015/12/label_font.png" width="811" /></a><p class="wp-caption-text" id="caption-attachment-656">Creating a variable for label font</p></div>
<p>Now, we can re-use that variable in a data defined override for the label font setting. In fact, QGIS makes this even easier for you by showing a &#8220;variables&#8221; sub-menu allowing easy access to all the currently defined variables accessible to the layer:</p>
<div class="wp-caption aligncenter" id="attachment_657" style="width: 997px;"><a href="http://nyalldawson.net/wp-content/uploads/2015/12/data_defined_font.png"><img alt="Binding the label font to the @main_label_font variable" class="wp-image-657 size-full" height="392" src="http://nyalldawson.net/wp-content/uploads/2015/12/data_defined_font.png" width="987" /></a><p class="wp-caption-text" id="caption-attachment-657">Binding the label font to the @main_label_font variable</p></div>
<p>&nbsp;</p>
<p>When we hit Apply all our labels will be updated to use the font face defined by the <em>@main_label_font</em> variable, so in this case &#8216;Courier New&#8217;:</p>
<p><img alt="courier_new" class="aligncenter wp-image-658 size-full" height="146" src="http://nyalldawson.net/wp-content/uploads/2015/12/courier_new.png" width="648" /></p>
<p>In a similar way we can bind all the other layer&#8217;s label fonts to the same variable, so <em>@main_label_font</em> will be reused by all the layers in the project. Then, when we later realise that Courier New was a horrible choice for labelling the map, it&#8217;s just a matter of opening up the Project Properties dialog and updating the value of the <em>@main_label_font</em> variable:</p>
<p><img alt="delicious" class="aligncenter wp-image-659 size-full" height="209" src="http://nyalldawson.net/wp-content/uploads/2015/12/delicious.png" width="612" /></p>
<p>And now when we hit Apply the font for all our labelled layers will be updated all at once:</p>
<p><img alt="new_labels" class="aligncenter size-full wp-image-660" height="135" src="http://nyalldawson.net/wp-content/uploads/2015/12/new_labels.png" width="591" /></p>
<p>It&#8217;s not only a huge time saver, it also makes changes like this easier because you can try out different font faces by updating the variable and hitting apply and seeing the effect that the changes have all at once. Updating multiple layers manually tends to have the consequence that you forget what the map looked like before you started making the change, making direct comparisons harder.</p>
<p>Of course, you could have multiple variables for other fonts used by your project too, eg <em>@secondary_label_font</em> and <em>@highlighted_feature_font</em>. Plus, this approach isn&#8217;t limited to just setting the label font. You could utilise project level variables for consolidating font sizes, symbol line thickness, marker rotation, in fact, ANYTHING that has one of those handy little data defined override buttons next to it:</p>
<div class="wp-caption aligncenter" id="attachment_661" style="width: 849px;"><a href="http://nyalldawson.net/wp-content/uploads/2015/12/datadefinedbuttons.png"><img alt="See all those nice little yellow buttons? All those controls can be bound to variables..." class="wp-image-661 size-full" height="536" src="http://nyalldawson.net/wp-content/uploads/2015/12/datadefinedbuttons.png" width="839" /></a><p class="wp-caption-text" id="caption-attachment-661">See all those nice little yellow buttons? All those controls can be bound to variables&#8230;</p></div>
<p>One last thing before I wrap up part 2 of this series. The same underlying changes which introduced variables to QGIS also allows us to begin introducing a whole stack of new, useful functions to the expression engine. One of these which also helps with project management is the new <em>project_color</em> function. Just like how we can use project level variables throughout a project, <em>project_color</em> lets you reuse a color throughout your project. First, you need to create a named colour in the Default Styles group under the Project Properties dialog:</p>
<div class="wp-caption aligncenter" id="attachment_662" style="width: 548px;"><img alt="Define a colour in the project's colour scheme..." class="size-full wp-image-662" height="193" src="http://nyalldawson.net/wp-content/uploads/2015/12/project_color.png" width="538" /><p class="wp-caption-text" id="caption-attachment-662">Define a colour in the project&#8217;s colour scheme&#8230;</p></div>
<p>Then, you can set a data defined override for a symbol or label colour to the expression &#8220;<em>project_color(&#8216;red alert!&#8217;)</em>&#8220;:</p>
<p><img alt="bind_color" class="aligncenter size-full wp-image-663" height="335" src="http://nyalldawson.net/wp-content/uploads/2015/12/bind_color.png" width="437" /></p>
<p>When you go back and change the corresponding colour in the Project Properties dialog, every symbol bound to this colour will also be updated!</p>
<p><img alt="blue_alert" class="aligncenter size-full wp-image-664" height="145" src="http://nyalldawson.net/wp-content/uploads/2015/12/blue_alert.png" width="713" /></p>
<p>So, there you have it. With a little bit of forward planning and by taking advantage of the power of expression variables in QGIS 2.12 you can help make your mapping projects much easier to manage and update!</p>
<p>That&#8217;s all for now, but we&#8217;re still only just getting started with variables. Part 3, coming soon!.. (Update: <a href="http://nyalldawson.net/2015/12/exploring-variables-in-qgis-pt-3-layer-level-variables/">Part 3</a> is available now)</p>
<p>&nbsp;</p>
