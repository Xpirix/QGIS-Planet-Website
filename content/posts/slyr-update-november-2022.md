---
source: "blog"
title: "SLYR Update — November 2022"
date: "2022-11-04T03:27:53+0000"
link: "https://north-road.com/2022/11/04/slyr-update-november-2022/"
draft: "false"
showcase: "planet"
subscribers: ["north_road"]
author: "North Road"
tags: ["qgis", "slyr", "aprx", "arcgis", "arcmap", "esri", "lyrx", "osgeo", "qgis", "slyr"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p><em><strong>Our <a href="https://north-road.com/slyr/">SLYR</a> tool is the complete solution for full compatibility between ArcMap, ArcGIS Pro and QGIS. It offers a powerful suite of conversion tools for opening ESRI projects, styles and other documents directly within QGIS, and for exporting QGIS documents for use in ESRI software.</strong></em></p>
<p>A lot has changed since our last SLYR product update post, and we’ve tons of very exciting improvements and news to share with you all! In this update we’ll explore some of the new tools we’ve added to SLYR, and discuss how these tools have drastically improved the capacity for users to migrate projects from the ESRI world to the open-source world (and vice versa).</p>
<h2>ArcGIS Pro support</h2>
<p>The headline item here is that SLYR now offers a powerful set of tools for working with the newer ArcGIS Pro document formats. Previously, SLYR offered support for the older ArcMap document types only (such as MXD, MXT, LYR, and PMF formats). Current SLYR versions now include tools for:</p>
<h3>Directly opening ArcGIS Pro .lyrx files within QGIS</h3>
<p>LYRX files can be dragged and dropped directly onto a QGIS window to add the layer to the current project. All the layer’s original styling and other properties will be automatically converted across, so the resultant layer will be an extremely close match to the original ArcGIS Pro layer! SLYR supports vector layers, raster layers, TIN layers, point cloud layers and vector tile layers. We take great pride in just how close the conversion results are to how these layers appear in ArcGIS Pro… in most cases you’ll find the results are nearly pixel perfect!</p>
<p>In addition to drag-and-drop import support, SLYR also adds support for showing .lyrx files directly in the integrated file browser, and also adds tools to the QGIS Processing Toolbox so that users can execute bulk conversion operations, or include document conversion in their models or custom scripts.</p>
<h3>ArcGIS Pro map (mapx) and project (aprx) conversion</h3>
<p>Alongside the LYRX support, we’ve also added support for the ArcGIS Pro .mapx and .aprx formats. Just like our existing .mxd conversion, you can now easily convert entire ArcGIS Pro maps for direct use within QGIS! SLYR supports both the older ArcGIS Pro 2.x project format and the newer 3.x formats.</p>
<h3>Export from QGIS to ArcGIS Pro!</h3>
<p>Yes, you read that correctly… SLYR now allows you to <strong>export QGIS documents into ArcGIS Pro formats</strong>! This is an extremely exciting development… for the first time <strong>ever</strong> QGIS users now have the capacity to export their work into formats which can be supplied directly to ESRI users. Current SLYR versions support conversion of map layers to .lyrx format, and exporting entire projects to the .mapx format. (<em>We’ll be introducing support for direct QGIS to .aprx exports later this year.</em>)</p>
<p>We’re so happy to finally provide an option for QGIS users to work alongside ArcGIS Pro users. This has long been a pain point for many organisations, and has even caused organisations to be ineligible to tender for jobs which they are otherwise fully qualified to do (when tenders require provision of data and maps in ArcGIS compatible formats).</p>
<h3>ArcGIS Pro .stylx support</h3>
<p>Alongside the other ArcGIS Pro documents, SLYR now has comprehensive support for <strong>reading</strong> and <strong>writing</strong> ArcGIS Pro .stylx databases. We’ve dedicated a ton of resources in ensuring that the conversion results (both from ArcGIS Pro to QGIS and from QGIS to ArcGIS Pro) are top-notch, and we even handle advanced ArcGIS Pro symbology options like symbol effects!</p>
<p>Take a look below how even very <a href="https://www.arcgis.com/home/item.html?id=3215e720f62d42008d125ca1a3219b14">advanced ArcGIS Pro style libraries</a> convert beautifully to QGIS symbol libraries:</p>
<p><img alt="" class="alignnone size-full wp-image-212441" height="678" src="/img/subscribers/north_road/slyr-update-november-2022/Screenshot-from-2022-11-04-12-39-06.webp" width="1353"/></p>
<h2>ArcMap Improvements</h2>
<p>While we’ve been focusing heavily on the newer ArcGIS Pro formats, we’ve also improved our support for the older ArcMap documents. In particular, SLYR now offers more options for converting ArcMap annotation layers and annotation classes to QGIS supported formats. Users can now convert Annotation layers and classes directly over to QGIS <a href="https://north-road.com/2021/10/21/introducing-annotation-layers-in-qgis-3-22/">annotation layer</a> or alternatively annotation classes can be converted over to the OGC standard GeoPackage format. When exporting annotation classes to GeoPackage the output database is automatically setup with default styling rules, so that the result can be opened directly in QGIS and will be immediately visualised to match the original annotation class.</p>
<h2>Coming soon…</h2>
<p>While all the above improvements are already available for all SLYR license holders, we’ve got many further improvements heading your way soon! For example, before the end of 2022 we’ll be releasing another large SLYR update which will introduce support for exporting QGIS projects directly to ArcGIS Pro .aprx documents. We’ve also got many enhancements planned which will further improve the quality of the converted documents. Keep an eye on this blog and our <a href="https://twitter.com/northroadgeo">social</a> <a href="https://www.linkedin.com/company/north-road-studios">media</a> <a href="https://mastodon.social/@northroadgeo@fosstodon.org">channels</a> for more details as they are available…</p>
<p><em><strong>You can read more about our SLYR tool at the <a href="https://north-road.com/slyr/">product page</a>, or <a href="https://north-road.com/contact/">contact us</a> today to discuss licensing options for your organisation.</strong></em></p>
<p> </p>
