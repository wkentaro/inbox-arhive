<?php
function article_imgs($article_url) {
  $html = @file_get_contents($article_url);
  $dom = @DOMDocument::loadHTML($html);
  $xml = simplexml_import_dom($dom);
  $data = $xml->xpath('//span[contains(@class, "mt-enclosure-image")]//img/@data-original');

  $img_srcs = array();
  foreach ($data as $v) {
    $img_srcs[] = (string)$v;
  }

  return $img_srcs;
}
