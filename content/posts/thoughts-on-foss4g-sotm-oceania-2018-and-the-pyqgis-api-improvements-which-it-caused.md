---
source: "blog"
title: "Thoughts on “FOSS4G/SOTM Oceania 2018”, and the PyQGIS API improvements which it caused"
date: "2018-11-25T00:05:07+0000"
link: "https://nyalldawson.net/2018/11/thoughts-on-foss4g-sotm-oceania-2018-and-the-pyqgis-api-improvements-which-it-caused/"
draft: "false"
showcase: "planet"
subscribers: ["nyalldawson_net"]
author: "nyalldawson.net"
tags: ["qgis", "foss4g", "geospatial", "osgeo", "pyqgis", "python", "qgis"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>Last week the first official “<a href="https://foss4g-oceania.org/">FOSS4G/SOTM Oceania</a>” conference was held at Melbourne University. This was a fantastic event, and there’s simply no way I can extend sufficient thanks to all the organisers and volunteers who put this event together. They did a brilliant job, and their efforts are even more impressive considering it was the inaugural event!</p>
<p><img alt="" class="aligncenter size-full wp-image-748" height="292" src="/img/subscribers/nyalldawson_net/thoughts-on-foss4g-sotm-oceania-2018-and-the-pyqgis-api-improvements-which-it-caused/logo.webp" width="500"/></p>
<p>Upfront — this is not a recap of the conference (I’m sure someone else is working on a much more detailed write up of the event!), just some musings I’ve had following my experiences assisting <a href="https://nathanw.net/" rel="noopener" target="_blank">Nathan Woodrow</a> deliver an introductory Python for QGIS workshop he put together for the conference. In short, we both found that delivering this workshop to a group of PyQGIS newcomers was a great way for us to identify “pain points” in the PyQGIS API and areas where we need to improve. The good news is that as a direct result of the experiences during this workshop the API has been improved and streamlined! Let’s explore how:</p>
<p>Part of Nathan’s workshop (notes are available <a href="https://madmanwoo.gitlab.io/foss4g-python-workshop/">here</a>) focused on a hands-on example of creating a custom QGIS “Processing” script. I’ve found that preparing workshops is guaranteed to expose a bunch of rare and tricky software bugs, and this was no exception! Unfortunately the workshop was scheduled just before the QGIS 3.4.2 patch release which fixed these bugs, but at least they’re fixed now and we can move on…</p>
<p>The bulk of Nathan’s example algorithm is contained within the following block (where “distance” is the length of line segments we want to chop our features up into):</p>
<pre class="brush: python; title: ; notranslate">
for input_feature in enumerate(features):
    geom = feature.geometry().constGet()
    if isinstance(geom, QgsLineString):
        continue
    first_part = geom.geometryN(0)
    start = 0
    end = distance
    length = first_part.length()

    while start &lt; length:
        new_geom = first_part.curveSubstring(start,end)

        output_feature = input_feature
        output_feature.setGeometry(QgsGeometry(new_geom))
        sink.addFeature(output_feature)

        start += distance
        end += distance
</pre>
<p>There’s a lot here, but really the guts of this algorithm breaks down to one line:</p>
<pre class="brush: python; title: ; notranslate">
new_geom = first_part.curveSubstring(start,end)
</pre>
<p>Basically, a new geometry is created for each trimmed section in the output layer by calling the “<a href="https://qgis.org/pyqgis/3.4/core/Curve/QgsCurve.html#qgis.core.QgsCurve.curveSubstring" rel="noopener" target="_blank">curveSubstring</a>” method on the input geometry and passing it a start and end distance along the input line. This returns the portion of that input LineString (or CircularString, or CompoundCurve) between those distances. The PyQGIS API nicely hides the details here – you can safely call this one method and be confident that regardless of the input geometry type the result will be correct.</p>
<p>Unfortunately, while calling the “curveSubstring” method is elegant, all the code surrounding this call is not so elegant. As a (mostly) full-time QGIS developer myself, I tend to look over oddities in the API. It’s easy to justify ugly API as just “how it’s always been”, and over time it’s natural to develop a type of blind spot to these issues.</p>
<p>Let’s start with the first ugly part of this code:</p>
<pre class="brush: python; title: ; notranslate">
geom = input_feature.geometry().constGet()
if isinstance(geom, QgsLineString):
    continue
first_part = geom.geometryN(0)
# chop first_part into sections of desired length
...
</pre>
<p>This is rather… confusing… logic to follow. Here the script is fetching the geometry of the input feature, checking if it’s a LineString, and if it IS, then it skips that feature and continues to the next. Wait… what? It’s skipping features with LineString geometries?</p>
<p>Well, yes. The algorithm was written specifically for one workshop, which was using a MultiLineString layer as the demo layer. The script takes a huge shortcut here and says “if the input feature isn’t a MultiLineString, ignore it — we only know how to deal with multi-part geometries”. Immediately following this logic there’s a call to <a href="https://qgis.org/pyqgis/3.4/core/Geometry/QgsGeometryCollection.html#qgis.core.QgsGeometryCollection.geometryN" rel="noopener" target="_blank">geometryN( 0 )</a>, which returns just the first part of the MultiLineString geometry.</p>
<p>There’s two issues here — one is that the script just plain won’t work for LineString inputs, and the second is that it ignores everything BUT the first part in the geometry. While it would be possible to fix the script and add a check for the input geometry type, put in logic to loop over all the parts of a multi-part input, etc, that’s instantly going to add a LOT of complexity or duplicate code here.</p>
<p>Fortunately, this was the perfect excuse to improve the PyQGIS API itself so that this kind of operation is simpler in future! Nathan and I had a debrief/brainstorm after the workshop, and as a result a new “parts iterator” has been implemented and merged to QGIS master. It’ll be available from version 3.6 on. Using the new iterator, we can simplify the script:</p>
<pre class="brush: python; title: ; notranslate">
geom = input_feature.geometry()
for part in geom.parts():
    # chop part into sections of desired length
    ...
</pre>
<p>Win! This is simultaneously more readable, more Pythonic, and automatically works for both LineString and MultiLineString inputs (and in the case of MultiLineStrings, we now correctly handle all parts).</p>
<p>Here’s another pain-point. Looking at the block:</p>
<pre class="brush: python; title: ; notranslate">
new_geom = part.curveSubstring(start,end)
output_feature = input_feature
output_feature.setGeometry(QgsGeometry(new_geom))
</pre>
<p>At first glance this looks reasonable – we use curveSubstring to get the portion of the curve, then make a copy of the input_feature as output_feature (this ensures that the features output by the algorithm maintain all the attributes from the input features), and finally set the geometry of the output_feature to be the newly calculated curve portion. The ugliness here comes in this line:</p>
<pre class="brush: python; title: ; notranslate">
output_feature.setGeometry(QgsGeometry(new_geom))
</pre>
<p>What’s that extra QgsGeometry(…) call doing here? Without getting too sidetracked into the QGIS geometry API internals, <a href="https://qgis.org/pyqgis/3.4/core/Feature/QgsFeature.html#qgis.core.QgsFeature.setGeometry" rel="noopener" target="_blank">QgsFeature.setGeometry</a> requires a <a href="https://qgis.org/pyqgis/3.4/core/Geometry/QgsGeometry.html" rel="noopener" target="_blank">QgsGeometry</a> argument, not the <a href="https://qgis.org/pyqgis/3.4/core/Abstract/QgsAbstractGeometry.html" rel="noopener" target="_blank">QgsAbstractGeometry</a> subclass which is returned by <a href="https://qgis.org/pyqgis/3.4/core/Curve/QgsCurve.html#qgis.core.QgsCurve.curveSubstring" rel="noopener" target="_blank">curveSubstring</a>.</p>
<p>This is a prime example of a “paper-cut” style issue in the PyQGIS API. Experienced developers know and understand the reasons behind this, but for newcomers to PyQGIS, it’s an obscure complexity. Fortunately the solution here was simple — and after the workshop Nathan and I added a new overload to QgsFeature.setGeometry which accepts a QgsAbstractGeometry argument. So in QGIS 3.6 this line can be simplified to:</p>
<pre class="brush: python; title: ; notranslate">
output_feature.setGeometry(new_geom)
</pre>
<p>Or, if you wanted to make things more concise, you could put the curveSubstring call directly in here:</p>
<pre class="brush: python; title: ; notranslate">
output_feature = input_feature
output_feature.setGeometry(part.curveSubstring(start,end))
</pre>
<p>Let’s have a look at the simplified script for QGIS 3.6:</p>
<pre class="brush: python; title: ; notranslate">
for input_feature in enumerate(features):
    geom = feature.geometry()
    for part in geom.parts():
        start = 0
        end = distance
        length = part.length()

        while start &lt; length:
            output_feature = input_feature
            output_feature.setGeometry(part.curveSubstring(start,end))
            sink.addFeature(output_feature)

            start += distance
            end += distance
</pre>
<p>This is MUCH nicer, and will be much easier to explain in the next workshop! The good news is that Nathan has more niceness on the way which will further improve the process of writing QGIS Processing script algorithms. You can see some early prototypes of this work here:</p>
<blockquote class="twitter-tweet">
<p dir="ltr" lang="en">I couldn’t be at the community day but managed to knock out some of the new API on the plane on the way home. **API subject to change <img alt="🙂" class="wp-smiley" src="/img/subscribers/nyalldawson_net/thoughts-on-foss4g-sotm-oceania-2018-and-the-pyqgis-api-improvements-which-it-caused/1f642.webp" style="height: 1em;"/><a href="https://twitter.com/hashtag/FOSS4G_SotM_Oceania?src=hash&amp;ref_src=twsrc%5Etfw">#FOSS4G_SotM_Oceania</a></p>
<p>cc <a href="https://twitter.com/nyalldawson?ref_src=twsrc%5Etfw">@nyalldawson</a> <a href="https://twitter.com/underdarkGIS?ref_src=twsrc%5Etfw">@underdarkGIS</a> this will create a alg under the hood and check for double inputs, etc <a href="https://t.co/49VpyuukGU">pic.twitter.com/49VpyuukGU</a></p>
<p>— Nathan Woodrow (@madmanwoo) <a href="https://twitter.com/madmanwoo/status/1065794574801559553?ref_src=twsrc%5Etfw">November 23, 2018</a></p></blockquote>
<p></p>
<p>So there we go. The process of writing and delivering a workshop helps to look past “API blind spots” and identify the ugly points and traps for those new to the API. As a direct result of this FOSS4G/SOTM Oceania 2018 Workshop, the QGIS 3.6 PyQGIS API will be easier to use, more readable, and less buggy! That’s a win all round!</p>
