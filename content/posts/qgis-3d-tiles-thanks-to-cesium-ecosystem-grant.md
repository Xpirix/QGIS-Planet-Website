---
source: "blog"
title: "QGIS 3D Tiles – thanks to Cesium Ecosystem Grant!"
date: "2023-11-07T04:27:34+0000"
link: "https://north-road.com/2023/11/07/qgis-3d-tiles-thanks-to-cesium-ecosystem-grant/"
draft: "false"
showcase: "planet"
subscribers: ["north_road"]
author: "North Road"
tags: ["3d tiles", "integrations", "qgis", "3d", "cesium", "osgeo", "qgis", "tiles"]
---

<p>We&#8217;ve recently had the opportunity to implement a very exciting feature in QGIS 3.34 &#8212; the ability to load and view 3D content in the &#8220;Cesium 3D Tiles&#8221; format! This was a joint project with our (very talented!) partners at <a class="ql-link" href="https://www.lutraconsulting.co.uk/" rel="noopener noreferrer" target="_blank">Lutra Consulting</a>, and was made possible thanks to a generous ecosystem grant from the <a href="https://cesium.com/">Cesium</a> project.</p>
<p>Before we dive into all the details, let&#8217;s take a quick guided tour showcasing how Cesium 3D Tiles work inside QGIS:</p>
<p></p>
<h2>What are 3D tiles?</h2>
<p>Cesium 3D Tiles are an OGC standard data format where the content from a 3D scene is split up into multiple individual tiles. You can think of them a little like a 3D version of the vector tile format we&#8217;ve all come to rely upon. The 3D objects from the scene are stored in a generalized, simplified form for small-scale, &#8220;zoomed out&#8221; maps, and in more detailed, complex forms for when the map is zoomed in. This allows the scenes to be incredibly detailed, whilst still covering huge geographic regions (including the whole globe!) and remaining responsive and quick to download. Take a look at the incredible level of detail available in a Cesium 3D Tiles scene in the example below:</p>
<p></p>
<h2>Where can you get 3D tile content?</h2>
<p>If you&#8217;re lucky, your regional government or data custodians are already publishing 3D &#8220;digital twins&#8221; of your area. Cesium 3D Tiles are the standard way that these digital twin datasets are being published. Check your regional data portals and government open data hubs and see whether they&#8217;ve made any content available as 3D tiles. (For Australian users, there&#8217;s tons of great content available on the <a href="https://www.csiro.au/en/research/technology-space/data/Terria">Terria</a> platform!).</p>
<p>Alternatively, there&#8217;s many datasets available via the <a href="https://ion.cesium.com/">Cesium ion</a> platform. This includes global 3D buildings based on OpenStreetMap data, and the entirety of Google&#8217;s photorealistic Google Earth tiles! We&#8217;ve published a <a href="https://plugins.qgis.org/plugins/cesium_ion/">Cesium ion QGIS plugin</a> to complement the QGIS 3.34 release, which helps make it super-easy to directly load datasets from ion into your QGIS projects.</p>
<p>Lastly, users of the <a href="https://www.opendronemap.org/">OpenDroneMap</a> photogrammetry application will already have Cesium 3D Tiles datasets of their projects available, as 3D tiles are one of the standard outputs generated by OpenDroneMap.</p>
<h2>Why QGIS?</h2>
<p>So why exactly would you want to access Cesium 3D tiles within QGIS? Well, for a start, 3D Tiles datasets are intrinsically <strong>geospatial</strong> data. All the 3D content from these datasets are georeferenced and have accurate spatial information present. By loading a 3D tiles dataset into QGIS, you can easily overlay and compare 3D tile content to all your other standard spatial data formats (such as Shapefiles, Geopackages, raster layers, mesh datasets, WMS layers, etc&#8230;). They become just another layer of spatial information in your QGIS projects, and  you can utilise all the tools and capabilities you&#8217;re familiar with in QGIS for analysing spatial data along with these new data sources.</p>
<p>One large drawcard of adding a Cesium 3D Tile dataset to your QGIS project is that they make <strong>fantastic</strong> 3D basemaps. While QGIS has had good support for 3D maps for a number of years now, it has been tricky to create beautiful 3D content. That&#8217;s because all the standard spatial data formats tend to give generalised, &#8220;blocky&#8221; representations of objects in 3D. For example, you could use an extruded building footprint file to show buildings in a 3D map but they&#8217;ll all be colored as idealised solid blocks. In contrast, Cesium 3D Tiles are a perfect fit for a 3D basemap! They typically include photorealistic textures, and include all types of real-world features you&#8217;d expect to see in a 3D map &#8212; including buildings, trees, bridges, cliffsides, etc.</p>
<h2>What next?</h2>
<p>If you&#8217;re keen to learn even more about Cesium 3D Tiles in QGIS, you can check out the recent <a href="https://www.youtube.com/live/vazJlXTcLsw?si=jNzI59y_Un-fHh1z">&#8220;QGIS Open Day&#8221; session</a> we presented. In this session we cover <strong>all</strong> the details about 3D tiles and QGIS, and talk in depth about what&#8217;s possible in QGIS 3.34 and what may be coming in later releases.</p>
<p>Otherwise, grab the latest QGIS 3.34 and start playing&#8230;. you&#8217;ll quickly find that Cesium 3D Tiles are a fun and valuable addition to QGIS&#8217; capabilities!</p>
<p><strong>Our thanks go to Cesium and their ecosystem grant project for funding this work and making it possible.</strong></p>
<div class="supsystic-social-sharing supsystic-social-sharing-package-flat supsystic-social-sharing-hide-on-homepage supsystic-social-sharing-spacing supsystic-social-sharing-content supsystic-social-sharing-content-align-left" style="font-size: 0.7em!important; display: none;"><a class="social-sharing-button sharer-flat sharer-flat-1 counter-standard without-counter twitter" href="https://twitter.com/share?url=https%3A%2F%2Fnorth-road.com%2F2023%2F11%2F07%2Fqgis-3d-tiles-thanks-to-cesium-ecosystem-grant%2F&amp;text=QGIS+3D+Tiles+%26%238211%3B+thanks+to+Cesium+Ecosystem+Grant%21" rel="nofollow" target="_blank" title="Twitter"><i class="fa-ssbs fa-ssbs-fw fa-ssbs-twitter"></i><div class="counter-wrap standard"><span class="counter">0</span></div></a><a class="social-sharing-button sharer-flat sharer-flat-1 counter-standard without-counter linkedin" href="https://www.linkedin.com/shareArticle?mini=true&amp;title=QGIS+3D+Tiles+%26%238211%3B+thanks+to+Cesium+Ecosystem+Grant%21&amp;url=https%3A%2F%2Fnorth-road.com%2F2023%2F11%2F07%2Fqgis-3d-tiles-thanks-to-cesium-ecosystem-grant%2F" rel="nofollow" target="_blank" title="Linkedin"><i class="fa-ssbs fa-ssbs-fw fa-ssbs-linkedin"></i><div class="counter-wrap standard"><span class="counter">0</span></div></a><a class="social-sharing-button sharer-flat sharer-flat-1 counter-standard without-counter facebook" href="http://www.facebook.com/sharer.php?u=https%3A%2F%2Fnorth-road.com%2F2023%2F11%2F07%2Fqgis-3d-tiles-thanks-to-cesium-ecosystem-grant%2F" rel="nofollow" target="_blank" title="Facebook"><i class="fa-ssbs fa-ssbs-fw fa-ssbs-facebook"></i><div class="counter-wrap standard"><span class="counter">0</span></div></a></div>