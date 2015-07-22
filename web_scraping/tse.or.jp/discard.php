<?php
function get_discard_company_stocks() {
  /*
   * 東証：上場廃止銘柄一覧
   * http://www.tse.or.jp/listing/haishi/list.html
  */
  $url = 'http://www.tse.or.jp/listing/haishi/list.html';
  $html = @file_get_contents($url);
  $dom = @DOMDocument::loadHTML($html);
  $xml = simplexml_import_dom($dom);
  $data = $xml->xpath('//table[@class="style01"]//tr');

  $stocks = array();
  for ($i=1; $max=count($data),$i<$max; $i++) {
    $stocks[] = array(
                  'discard_date'   => trim((string)$data[$i]->td[1]),
                  'stock_code'     => trim((string)$data[$i]->td[2]),
                  'company_name'   => trim((string)$data[$i]->td[3]),
                  'market_segment' => trim((string)$data[$i]->td[4]),
                  'discard_reason' => trim((string)$data[$i]->td[5])
                );
  }

  return $stocks;
}
var_dump(get_discard_company_stocks());
