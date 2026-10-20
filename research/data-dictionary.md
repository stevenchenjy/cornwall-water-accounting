# Annual water table

| Field | Meaning / unit |
|---|---|
| reporting_year | 报告标明的数据年度，不是上传或出版年 |
| period_start / period_end | 原文明确的数据期；未核对留空 |
| pws_id | 原文系统编号，不能据地方名称推断 |
| produced_gal | 原文全年生产/供水量，US gallons |
| reported_daily_produced_gal | 原文日均总供水量，gal/day |
| reported_daily_billed_gal | 原文日均计费用水量，gal/day |
| reported_unaccounted_pct | 原文百分比，0–100，非小数分数 |
| source_id / physical_pdf_page | 来源表的稳定标识 / PDF 物理页码（1 起算） |
| verification_status | pending_extraction / source_text_checked / human_verified |
| derived_annual_billed_gal | 程序推算，日均计费量×365/366；不是观测年度合计 |

数值空白表示缺失，不能置零。来源 SHA 和抓取时间通过 source_id 联到 data/manifests/retrievals.csv。
