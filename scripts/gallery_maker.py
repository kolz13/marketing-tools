#!/usr/bin/python

import cgitb, cgi
import os
import pandas as pd
import io
import sys

path = os.path.abspath(__file__)
sys.path.append(os.path.join(os.path.dirname(path), "../"))

from html_template import header as template_header

cgitb.enable()
print("Content-type: text/html")
print("")

form = cgi.FieldStorage()
csv = form['csv']

df = pd.read_csv(csv.file)

 
def gallery(df):
    g = io.StringIO()

    header = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Slider Theme - Jssor Slider, Carousel, Slideshow with Javascript Source Code</title>
    <META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
</head>
<body style="font-family:Arial, Verdana;background-color:#fff;">
    <!-- Caption Style -->

    <!-- it works the same with all jquery version from 1.x to 2.x -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <!-- use jssor.slider.mini.js (40KB) instead for release -->
    <!-- jssor.slider.mini.js = (jssor.js + jssor.slider.js) -->
    <script type="text/javascript" src="https://www.homesnacks.net/js-files/jssor.slider.mini.js"></script>
    <script>

        jQuery(document).ready(function ($) {
            var options = {
                $AutoPlay: false,                                    //[Optional] Whether to auto play, to enable slideshow, this option must be set to true, default value is false
                $AutoPlaySteps: 1,                                  //[Optional] Steps to go for each navigation request (this options applys only when slideshow disabled), the default value is 1
                $AutoPlayInterval: 4000,                            //[Optional] Interval (in milliseconds) to go for next slide since the previous stopped if the slider is auto playing, default value is 3000
                $PauseOnHover: 1,                               //[Optional] Whether to pause when mouse over if a slider is auto playing, 0 no pause, 1 pause for desktop, 2 pause for touch device, 3 pause for desktop and touch device, 4 freeze for desktop, 8 freeze for touch device, 12 freeze for desktop and touch device, default value is 1

                $ArrowKeyNavigation: true,                           //[Optional] Allows keyboard (arrow key) navigation or not, default value is false
                $SlideDuration: 500,                                //[Optional] Specifies default duration (swipe) for slide in milliseconds, default value is 500
                $MinDragOffsetToSlide: 20,                          //[Optional] Minimum drag offset to trigger slide , default value is 20
                //$SlideWidth: 600,                                 //[Optional] Width of every slide in pixels, default value is width of 'slides' container
                //$SlideHeight: 300,                                //[Optional] Height of every slide in pixels, default value is height of 'slides' container
                $SlideSpacing: 0,                                     //[Optional] Space between each slide in pixels, default value is 0
                $DisplayPieces: 1,                                  //[Optional] Number of pieces to display (the slideshow would be disabled if the value is set to greater than 1), the default value is 1
                $ParkingPosition: 0,                                //[Optional] The offset position to park slide (this options applys only when slideshow disabled), default value is 0.
                $UISearchMode: 1,                                   //[Optional] The way (0 parellel, 1 recursive, default value is 1) to search UI components (slides container, loading screen, navigator container, arrow navigator container, thumbnail navigator container etc).
                $PlayOrientation: 1,                                //[Optional] Orientation to play slide (for auto play, navigation), 1 horizental, 2 vertical, 5 horizental reverse, 6 vertical reverse, default value is 1
                $DragOrientation: 3,                                //[Optional] Orientation to drag slide, 0 no drag, 1 horizental, 2 vertical, 3 either, default value is 1 (Note that the $DragOrientation should be the same as $PlayOrientation when $DisplayPieces is greater than 1, or parking position is not 0)

                $ArrowNavigatorOptions: {
                    $Class: $JssorArrowNavigator$,              //[Requried] Class to create arrow navigator instance
                    $ChanceToShow: 1,                               //[Required] 0 Never, 1 Mouse Over, 2 Always
                    $AutoCenter: 2,                                 //[Optional] Auto center arrows in parent container, 0 No, 1 Horizontal, 2 Vertical, 3 Both, default value is 0
                    $Steps: 1                                       //[Optional] Steps to go for each navigation request, default value is 1
                },

                $ThumbnailNavigatorOptions: {
                    $Class: $JssorThumbnailNavigator$,              //[Required] Class to create thumbnail navigator instance
                    $ChanceToShow: 2,                               //[Required] 0 Never, 1 Mouse Over, 2 Always

                    $ActionMode: 1,                                 //[Optional] 0 None, 1 act by click, 2 act by mouse hover, 3 both, default value is 1
                    $AutoCenter: 3,                                 //[Optional] Auto center thumbnail items in the thumbnail navigator container, 0 None, 1 Horizontal, 2 Vertical, 3 Both, default value is 3
                    $Lanes: 1,                                      //[Optional] Specify lanes to arrange thumbnails, default value is 1
                    $SpacingX: 3,                                   //[Optional] Horizontal space between each thumbnail in pixel, default value is 0
                    $SpacingY: 3,                                   //[Optional] Vertical space between each thumbnail in pixel, default value is 0
                    $DisplayPieces: 9,                              //[Optional] Number of pieces to display, default value is 1
                    $ParkingPosition: 260,                          //[Optional] The offset position to park thumbnail
                    $Orientation: 1,                                //[Optional] Orientation to arrange thumbnails, 1 horizental, 2 vertical, default value is 1
                    $DisableDrag: false                            //[Optional] Disable drag or not, default value is false
                }
            };
            var jssor_slider2 = new $JssorSlider$("slider2_container", options);
            //responsive code begin
            //you can remove responsive code if you don't want the slider scales while window resizes
            function ScaleSlider() {
                var parentWidth = jssor_slider2.$Elmt.parentNode.clientWidth;
                if (parentWidth)
                    jssor_slider2.$ScaleWidth(Math.min(parentWidth, 900));
                else
                    window.setTimeout(ScaleSlider, 30);
            }
            ScaleSlider();

            $(window).bind("load", ScaleSlider);
            $(window).bind("resize", ScaleSlider);
            $(window).bind("orientationchange", ScaleSlider);
            //responsive code end
        });
    </script>
    <!-- Jssor Slider Begin -->
    <!-- To move inline styles to css file/block, please specify a class name for each element. -->
    <div id="slider2_container" style="position: relative; top: 0px; left: 0px; width: 900px; height: 500px; overflow: hidden; ">

        <!-- Loading Screen -->
        <div u="loading" style="position: absolute; top: 0px; left: 0px;">
            <div style="filter: alpha(opacity=70); opacity:0.7; position: absolute; display: block;
                background-color: #000000; top: 0px; left: 0px;width: 100%;height:100%;">
            </div>
            <div style="position: absolute; display: block; background: url(https://www.homesnacks.net/images/widgets/gallery/loading.gif) no-repeat center center;
                top: 0px; left: 0px;width: 100%;height:100%;">
            </div>
        </div>

        <!-- Slides Container -->
        <div u="slides" style="cursor: move; position: absolute; left: 0px; top: 0px; width: 900px; height: 500px; overflow: hidden;">"""

    places = ''
    for index, row in df.iterrows():
        context = {'count' : index + 1,
                   'place' : row['place'],
                   'image_url' : row['url']}
        places += """<div>
    <div u="image" class="big-guy">
        <h2>#{count} - {place}</h2>
        <img  src='{image_url}' />
    </div>
    <div u="thumb" >
        <img src='{image_url}' class="t"/>
        <h2>#{count}<h2>
    </div>
</div>""".format(**context)

    #closes the container div and the content div. It then adds the standard website footer.
    footer = """       </div>

        <!--#region Arrow Navigator Skin Begin -->
        <!-- Help: https://www.jssor.com/development/slider-with-arrow-navigator-jquery.html -->
        <style>
            /* jssor slider arrow navigator skin 02 css */
            /*
            .jssora02l                  (normal)
            .jssora02r                  (normal)
            .jssora02l:hover            (normal mouseover)
            .jssora02r:hover            (normal mouseover)
            .jssora02l.jssora02ldn      (mousedown)
            .jssora02r.jssora02rdn      (mousedown)
            */
            .jssora02l, .jssora02r {
                display: block;
                position: absolute;
                /* size of arrow element */
                width: 55px;
                height: 55px;
                cursor: pointer;
                background: url(https://www.homesnacks.net/images/widgets/gallery/a02.png) no-repeat;
                overflow: hidden;
            }
            .jssora02l { background-position: -3px -33px; }
            .jssora02r { background-position: -63px -33px; }
            .jssora02l:hover { background-position: -123px -33px; }
            .jssora02r:hover { background-position: -183px -33px; }
            .jssora02l.jssora02ldn { background-position: -3px -33px; }
            .jssora02r.jssora02rdn { background-position: -63px -33px; }
        </style>
        <!-- Arrow Left -->
        <span u="arrowleft" class="jssora02l" style="top: 123px; left: 8px;">
        </span>
        <!-- Arrow Right -->
        <span u="arrowright" class="jssora02r" style="top: 123px; right: 8px;">
        </span>
        <!--#endregion Arrow Navigator Skin End -->
        <!--#region Thumbnail Navigator Skin Begin -->
        <!-- Help: https://www.jssor.com/development/slider-with-thumbnail-navigator-jquery.html -->
        <style>
            /* jssor slider thumbnail navigator skin 03 css */
            /*
            .jssort03 .p            (normal)
            .jssort03 .p:hover      (normal mouseover)
            .jssort03 .pav          (active)
            .jssort03 .pdn          (mousedown)
            */

            .jssort03 {
                position: absolute;
                /* size of thumbnail navigator container */
                width: 900px;
                height: 90px;
            }

                .jssort03 .p {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 120px;
                    height: 90px;
                }

                .jssort03 .t {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    border: none;
                    color:white;
                    line-height:2em;
                }
                .jssort03 .t h2{
                    position: absolute;
                    top: 0;
                    left: 0;
                    margin:0px;
                    padding:0px;
                    font-size:1em;
                    background: black;
                    opacity: .5;
                    width:25%;
                }

                .jssort03 .w, .jssort03 .pav:hover .w {
                    position: absolute;
                    width: 100%;
                    height: 100%;
                    border: white 1px dashed;
                    box-sizing: content-box;
                }

                .jssort03 .pdn .w, .jssort03 .pav .w {
                    border-style: solid;
                }

                .jssort03 .c {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background-color: #000;
                    filter: alpha(opacity=45);
                    opacity: .45;
                    transition: opacity .6s;
                    -moz-transition: opacity .6s;
                    -webkit-transition: opacity .6s;
                    -o-transition: opacity .6s;
                }

                .jssort03 .p:hover .c, .jssort03 .pav .c {
                    filter: alpha(opacity=0);
                    opacity: 0;
                }

                .jssort03 .p:hover .c {
                    transition: none;
                    -moz-transition: none;
                    -webkit-transition: none;
                    -o-transition: none;
                }

                * html .jssort03 .w {
                    width /**/: 100%;
                    height /**/: 100%;
                }

                @media (max-width: 400px){
                    .jssort03{
                        display:none;
                    }
                }

                .big-guy{
                    height: inherit;
                }

                .big-guy h2{
                    margin: 0px;
                    padding: 20px;
                    position: absolute;
                    color: white;
                    background: black;
                    opacity: .7;
                    z-index: 100;
                }
            .big-guy img{
                height:inherit;
                width:100%;
            }
        </style>

        <!-- thumbnail navigator container -->
        <div u="thumbnavigator" class="jssort03" style="left: 0px; bottom: 0px;">

            <!-- the following background element is optional -->
            <div style=" background-color: #000; filter:alpha(opacity=30); opacity:.3; width: 100%; height:100%;"></div>

            <!-- Thumbnail Item Skin Begin -->
            <div u="slides" style="cursor: default;">
                <div u="prototype" class="p">
                    <div class=w><div u="thumbnailtemplate" class="t"></div></div>
                    <div class=c></div>
                </div>
            </div>
            <!-- Thumbnail Item Skin End -->
        </div>
        <!--#endregion Thumbnail Navigator Skin End -->
        <a style="display: none" href="https://www.jssor.com">Carousel Slider</a>
    </div>
    <!-- Jssor Slider End -->
</body>
</html>"""

    g.write(header)
    g.write(places)
    g.write(footer)
    content = g.getvalue()
    g.close()
    return content

gallery_html = gallery(df)

html = '<body><h2>Copy this code into an empty .html file.</h2><br><textarea style="width:100%;height:500px;">{}</textarea></body></html>'.format(gallery_html)

context = {'head' : ''}
print(template_header.format(**context))
print(html)