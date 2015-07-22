<?php

function matome_imgs($matome_url) {
  $html = @file_get_contents($matome_url);
  $dom = @DOMDocument::loadHTML($html);
  $xml = simplexml_import_dom($dom);
  $img_urls = $xml->xpath('//p[@class="mdMTMWidget01ItemImg01View"]/a/@href');

  $img_srcs = array();
  foreach ($img_urls as $v) {
    $img_url = (string)$v;
    if (strpos($img_url, 'gettyimages')) {
      if ($tmp = gettyimages_img_src($img_url)) {
        $img_srcs[] = $tmp;
      }
    } elseif (strpos($img_url, 'amanaimages')) {
      if ($tmp = amanaimages_img_src($img_url)) {
        $img_srcs[] = $tmp;
      }
    }
  }
  var_dump($img_srcs);
}

function gettyimages_img_src($url) {
  echo 'cannot crawl this page'.$url."\n";
}

function amanaimages_img_src($url) {
  if (!$html = @file_get_contents($url)) {
    echo 'cannot crawl this page'.$url."\n";
    return;
  }
  $dom = @DOMDocument::loadHTML($html);
  $xml = simplexml_import_dom($dom);
  $img_src = $xml->xpath('//img[@id="imgPhoto"]/@src');
  return (string)$img_src[0]->src[0];
}

matome_imgs('http://matome.naver.jp/odai/2138751680330961901');
