---
source: "blog"
title: "Creating circular insets and other fun QGIS layout tricks"
date: "2022-11-04T03:05:00+0000"
link: "https://north-road.com/2022/11/04/creating-circular-insets-and-other-fun-qgis-layout-tricks/"
draft: "false"
showcase: "planet"
subscribers: ["north_road"]
author: "North Road"
tags: ["cartography", "qgis", "cartography", "composer", "html", "layouts", "qgis"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p><em><strong>Thanks to the recent popularity of the “<a href="https://twitter.com/hashtag/30DayMapChallenge">30 Day Map Challenge</a>“, the month of November has become synonymous with beautiful maps and cartography. During this November we’ll be sharing a bunch of tips and tricks which utilise some advanced QGIS functionality to help create beautiful maps.</strong></em></p>
<p>One technique which can dramatically improve the appearance of maps is to swap out rectangular inset maps for more organic shapes, such as circles or ovals.</p>
<p>Back in 2020, we had the opportunity to add support for directly creating circular insets in QGIS Print Layouts (thanks to sponsorship from the City of Canning, Australia!). While this functionality makes it easy to create non-rectangular inset maps the steps, many QGIS users may not be aware that this is possible, so we wanted to highlight this functionality for our first 30 Day Map Challenge post.</p>
<p>Let’s kick things off with an example map. We’ve shown below an extract from the <a href="https://stillmed.olympics.com/media/Documents/Olympic-Games/Brisbane-2032/General/IOC-Feasibility-Assessment-Brisbane.pdf?_ga=2.48780838.1295957495.1666960789-1227590087.1665520398">2032 Brisbane Olympic Bid</a> that some of the North Road team helped create (on behalf of <a href="https://www.smec.com/au/">SMEC </a>for <a href="https://www.eks.com">EKS</a>). This map is designed to highlight potential venues around South East Queensland and the travel options between these regions:</p>
<figure class="wp-caption aligncenter" id="attachment_212431" style="width: 719px;"><a href="https://stillmed.olympics.com/media/Documents/Olympic-Games/Brisbane-2032/General/IOC-Feasibility-Assessment-Brisbane.pdf?_ga=2.48780838.1295957495.1666960789-1227590087.1665520398"><img alt="Venue Masterplan Brisbane 2032 Olympics" class="wp-image-212431" height="732" src="/img/subscribers/north_road/creating-circular-insets-and-other-fun-qgis-layout-tricks/Olympic-map-2-1006x1024.webp" width="719"/></a><figcaption class="wp-caption-text" id="caption-attachment-212431">Venue Masterplan for 2032 Olympic Games, IOC Feasibility Assessment – Olympic Games, Brisbane February 2021</figcaption></figure>
<p>Circles featured heavily in previous Olympic bid maps (such as Budapest) where we took our inspiration from. This may, or may not, play a part in using the language of the target map audience – think Olympic rings!</p>
<p style="text-align: center;"><a href="https://architectureofthegames.net/tag/budapest/"><img alt="Budapest Olympics 2024 Masterplan" class="wp-image-212407 aligncenter" height="470" src="/img/subscribers/north_road/creating-circular-insets-and-other-fun-qgis-layout-tricks/2024-Bid-Masterplan-Budapest-2024-1-1024x691.webp" width="696"/></a>Budapest Olympics 2024 Masterplan</p>
<p> </p>
<h3>Step by Step Guide to Creating a Circle Inset</h3>
<p>Firstly, prepare a print layout with both a main map and an inset map. Make sure that your inset map is large enough to cover your circular shape:</p>
<p><img alt="" class="wp-image-212432 alignnone" height="451" src="/img/subscribers/north_road/creating-circular-insets-and-other-fun-qgis-layout-tricks/base-map-1024x730.webp" width="633"/></p>
<p>From the Print Layout toolbar, click on the <b>Add Shape</b> button and then select <strong>Add </strong><strong>Ellipse</strong><i>:</i></p>
<p><img alt="" class="wp-image-212421 alignnone" height="164" src="/img/subscribers/north_road/creating-circular-insets-and-other-fun-qgis-layout-tricks/add-shape.webp" width="250"/></p>
<p>Draw the ellipse over the middle of your inset map (hint: holding down Shift while drawing the ellipse will force it to a circular shape!). If you didn’t manage to create an exact circle then you can manually specify the width and height in the shape item’s properties. For this one, we went with a 50mm x 50mm circle:</p>
<p><img alt="" class="alignnone wp-image-212410" height="352" src="/img/subscribers/north_road/creating-circular-insets-and-other-fun-qgis-layout-tricks/Ellipse-measurements.webp" width="577"/></p>
<p>Next, select the Inset Map item and in its <strong>Item Properties</strong> click on the <b>Clipping Settings button:</b></p>
<p><img alt="" class="alignnone size-full wp-image-212409" height="90" src="/img/subscribers/north_road/creating-circular-insets-and-other-fun-qgis-layout-tricks/clipping-settings.webp" width="393"/></p>
<p>In the <b>Clipping Settings</b>, scroll down to the second section and tick the <i>Clip to Item</i> box and select your Ellipse item from the list. (If you have labels shown in your inset map you may also want to check the “force labels inside clipping shape” option to force these labels inside the circle. If you don’t check this option then labels will be allowed to overflow outside of the circle shape.)</p>
<p><img alt="" class="alignnone size-full wp-image-212426" height="186" src="/img/subscribers/north_road/creating-circular-insets-and-other-fun-qgis-layout-tricks/clipping-settings2.webp" width="552"/></p>
<p>Your inset map will now be bound to the ellipse!</p>
<p><img alt="" class="alignnone size-full wp-image-212408" height="427" src="/img/subscribers/north_road/creating-circular-insets-and-other-fun-qgis-layout-tricks/clipped-inset.webp" width="478"/></p>
<p>Here’s a bit more magic you could add to this map – in the Main Map’s properties, click on <i>Overviews</i> and set create one for the Inset map – it will nicely show the visible circular area and not the rectangle!</p>
<p><img alt="" class="alignnone size-full wp-image-212413" height="537" src="/img/subscribers/north_road/creating-circular-insets-and-other-fun-qgis-layout-tricks/overview-map.webp" width="829"/></p>
<h3>Bonus Points: Circular Title Text!</h3>
<p>For advanced users, we’ve another fun tip…and when we say fun, we mean ‘let’s play with radians’! Here we’re going to create some title text and a wedged background which curves around the outside of our circular inset. This takes some fiddly playing around, but the end result can be visually striking! Here we’re going to push the QGIS print layout “HTML” item to create some advanced graphics, so some HTML and CSS coding experience is advantageous. (An alternative approach would be to use a vector illustration application like <a href="https://inkscape.org/">Inkscape</a>, and add your title and circular background as an SVG item in the print layout).</p>
<p>We’ll start by creating some curved circular text:</p>
<p><img alt="" class="alignnone size-full wp-image-212415" height="239" src="/img/subscribers/north_road/creating-circular-insets-and-other-fun-qgis-layout-tricks/text.webp" width="265"/></p>
<p>First, add a “HTML frame” to your print layout:</p>
<p><img alt="" class="alignnone size-full wp-image-212411" height="77" src="/img/subscribers/north_road/creating-circular-insets-and-other-fun-qgis-layout-tricks/html-frame-tool.webp" width="113"/></p>
<p>HTML frames allow placement of dynamic content in your layouts, which can use HTML, CSS and JavaScript to create graphical components.</p>
<p>In the HTML item’s “<strong>source”</strong> box, add the following code:</p>
<pre>&lt;svg height="300" width="350"&gt;
        &lt;defs&gt;
            &lt;clipPath id="circleView"&gt;
                &lt;circle id="curve" cx="183" cy="156" r="25" fill="transparent" /&gt;
            &lt;/clipPath&gt;
        &lt;/defs&gt;
        &lt;path id="forText" d="M 28,150, C 25,50, 180,-32,290,130" stroke="" fill="none"/&gt;
            &lt;text x="0" y="35" width="100"&gt;
                &lt;textpath xlink:href="#forText"&gt;
                    &lt;tspan font-weight="bold" fill="black"&gt;Place text here&lt;/tspan&gt;
                &lt;/textpath&gt;
            &lt;/text&gt;
             &lt;style&gt;
    &lt;![CDATA[
      text{
        dominant-baseline: hanging;
        font: 20px Arial;
      }
    ]]&gt;
  &lt;/style&gt;
&lt;/svg&gt;</pre>
<p>Now, let’s add in a background to bring more focus onto the title!</p>
<p><img alt="" class="alignnone size-medium wp-image-212427" height="277" src="/img/subscribers/north_road/creating-circular-insets-and-other-fun-qgis-layout-tricks/text-with-background-1-300x277.webp" width="300"/></p>
<p>To add in the background, create another HTML item. We’ll again create the arc shape using an SVG element, so add the following code into the item’s <strong>source</strong> box:</p>
<pre>&lt;svg width="750" height="750" xmlns="http://www.w3.org/2000/svg"&gt;
  &lt;path d="M 90 70
           A 56 56, 0, 0, 0, 133 140
           L 150 90 Z" fill="#414042" transform=" scale(2.1) rotate(68 150 150) " /&gt;/&gt;
&lt;/svg&gt;</pre>
<p>(You can read more about <a href="https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths">SVG  curves and arcs paths over</a> at MDN<a href="https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths">)</a></p>
<p><em><strong>So there we go! These two techniques can help push your QGIS map creations further and make it easier to create beautiful cartography directly in QGIS itself. If you found these tips useful, keep an eye on this blog as we post more tips and tricks over the month of November. And don’t forget to follow the <a href="https://30daymapchallenge.com/">30 day Map Challenge</a> for a smorgasbord of absolutely stunning maps.</strong></em></p>
