# **Marketing Analytics Dashboard – Power BI**

## **1\. Описание**

Дашборд построен на основе таблицы `final_metrics`, объединяющей данные по рекламным кампаниям Facebook Ads, Google Ads и MMP.

Цель: визуально оценивать эффективность рекламных кампаний, метрики затрат, установок, кликов и дохода.

---

## **2\. Загрузка и подготовка данных**

* Данные загружены через Power Query из CSV/SQL.

* Преобразованы типы столбцов для корректной агрегации: дата, числа, текст.

* Создана единая таблица `final_metrics`, на основе которой строятся меры и визуализации.

---

## **3\. Созданные меры (DAX)**

1. **Spend**

`Spend = SUM(final_metrics[spend])`

2. **Installs (MMP)**

`Installs = SUM(final_metrics[mmp_installs])`

3. **Clicks**

`Clicks = SUM(final_metrics[clicks])`

4. **Impressions**

`Impressions = SUM(final_metrics[impressions])`

5. **CTR**

`CTR = DIVIDE(SUM(final_metrics[clicks]), SUM(final_metrics[impressions]))`

6. **CPI**

`CPI = DIVIDE(SUM(final_metrics[spend]), SUM(final_metrics[mmp_installs]))`

7. **ROAS D1**

`ROAS_D1 = DIVIDE(SUM(final_metrics[d1_revenue]), SUM(final_metrics[spend]))`

8. **ROAS D7**

`ROAS_D7 = DIVIDE(SUM(final_metrics[d7_revenue]), SUM(final_metrics[spend]))`

---

## **4\. Визуализации**

1. **Карточки KPI**

* Spend

* Installs

* Clicks

* Impressions

* CTR

* CPI

* ROAS D1 / D7

2. **Диаграммы по дням** (линии)

* Spend

* Installs

* Date

  

3. **Таблица по кампаниям**

* Spend

* Installs

* Clicks

* Impressions

* CPI

* ROAS D1 / D7

4. **Срезы (Slicers)**

* Источник (FB / Google)

* Период (дата)

---

## **5\. Итог**

Дашборд позволяет:

* Сразу видеть суммарные KPI за выбранный период

* Сравнивать эффективность кампаний по источникам и датам

* Отслеживать динамику затрат, установок, кликов и дохода

* Использовать показатели CPI, CTR и ROAS для принятия решений по оптимизации кампаний

