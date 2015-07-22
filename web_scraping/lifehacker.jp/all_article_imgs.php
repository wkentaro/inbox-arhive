<?php
include_once(dirname(__FILE__).'/include/article_imgs.php');
include_once(dirname(__FILE__).'/include/all_article_urls.php');

echo 'crawling ..';

// create article urls' array
$article_urls = all_article_urls(2000, date('Y'));

// prepare to write srcs on text file
$img_srcs = '';
foreach ($article_urls as $v_article_url) {
  foreach (article_imgs($v_article_url) as $v) {
    $img_srcs .= $v."\n";
  }
}

file_put_contents('srcs_all_article_imgs.dat', $img_srcs);

echo "finished!\n";
