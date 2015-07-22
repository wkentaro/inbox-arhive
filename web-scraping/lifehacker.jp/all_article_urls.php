<?php

function all_article_urls($start_year, $end_year) {
  if (!isset($start_year)) {
    $start_year = date('Y');
  }
  if (!isset($end_year)) {
    $start_year = date('Y');
  }
  $top_url = 'http://www.lifehacker.jp';
  $article_urls = array();

  // year repository of url
  for ($y = $start_year; $y <= $end_year; $y++) {
    // month repository of url
    for ($m = 1; $m <= 12; $m++) {
      $i = 1;
      $url = $top_url.'/'.$y.'/'.sprintf('%02d', $m);
      while ($html = @file_get_contents($url)) {
        // get link data
        $dom = @DOMDocument::loadHTML($html);
        $xml = simplexml_import_dom($dom);
        $data = $xml->xpath('//div[contains(@class, "entry")]/h2/a/@href');
        foreach ($data as $v) {
          $article_urls[] = (string)$v;
        }

        // generate next url
        $url = $top_url.'/'.$y.'/'.sprintf('%02d', $m).'/'.$i.'.html';

        $i++;
      }
    }
  }

  return $article_urls;
}
