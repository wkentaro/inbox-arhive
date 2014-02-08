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

$stocks = get_discard_company_stocks();

$to = 'www.kentaro.wada@gmail.com';
$subject = '東証：上場廃止日一覧 ' . date('Y/m/d');
$message = '<html><body><table style="border-collapse:collapse;">';
$message .= '<tr>
              <th style="border:solid 1px #dddddd;">No.</th>
              <th style="border:solid 1px #dddddd;">廃止日</th>
              <th style="border:solid 1px #dddddd;">コード</th>
              <th style="border:solid 1px #dddddd;">会社名</th>
              <th style="border:solid 1px #dddddd;">区分</th>
              <th style="border:solid 1px #dddddd;">理由</th>
            </tr>';
for ($i=0; $max=count($stocks),$i<$max; $i++) {
  $message .= '<tr>
                <td style="border:solid 1px #dddddd;">' . ($i+1)                        . '</td>
                <td style="border:solid 1px #dddddd;">' . $stocks[$i]['discard_date']   . '</td>
                <td style="border:solid 1px #dddddd;">' . $stocks[$i]['stock_code']     . '</td>
                <td style="border:solid 1px #dddddd;">' . $stocks[$i]['company_name']   . '</td>
                <td style="border:solid 1px #dddddd;">' . $stocks[$i]['market_segment'] . '</td>
                <td style="border:solid 1px #dddddd;">' . $stocks[$i]['discard_reason'] . '</td>
              </tr>';
}
$message .= '</table></body></html>';
$headers = 'MIME-Version: 1.0' . "\r\n" . 
           'Content-type: text/html; charset=ISO-2022-JP' . "\r\n" .
           'From: DEV<dev@kwh.mobi>' . "\r\n" .
           'Reply-To: dev@kwh.mobi' . "\r\n" .
           'X-Mailer: PHP/' . phpversion();

mail($to, mb_encode_mimeheader($subject, 'ISO-2022-JP-MS'), mb_convert_encoding($message, 'ISO-2022-JP-MS'), $headers);
