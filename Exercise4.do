import excel https://github.com/jaycka/financialdataanalysis/blob/master/Data.xls, sheet("Transaction") firstrow
gen date_id = mdy(month,day,year)

format date_id %tdCCYY-NN-DD
sort product_id date_id
by product_id date_id: gen quantity2 =sum(quantity)
by product_id date_id: egen quantity_sold = max(quantity2)
drop quantity2
duplicates drop product_id date_id,force
save "C:\Users\Day19\Desktop\b.dta
clear
import excel https://github.com/jaycka/financialdataanalysis/blob/master/Data.xls, sheet("Product") firstrow
gen date_id = mdy(month,day,year)
format date_id %tdCCYY-NN-DD
sort product_id date_id
cd "C:\Users\Day19\Desktop"
merge product_id date_id using b.dta
replace quantity_sold = 0 if quantity_sold>=.
drop if price<=0 | price==.
drop id buyer_name quantity _merge
order product_id date_id year month day quantity_sold review_volume review_rating price

* (1) Report the descriptive statistics table (number of observations, mean, standard deviation, min, max).
sum

* (2) Report the correlation table (with/without significance).
corr
pwcorr,sig

* (3) How many different products in total in the data sample?
unique product_id

* (4) How many different days in total in the data sample?
unique date_id

* (5) Is this a balanced panel dataset?
* Kinda, it is since it provides the full daily transaction record on day-to-day basis for 3 consecutive months.

* (6) What is the price of the most expensive product in the store on July 1, 2012?
sort date_id price

* (7) What is the average price and number of reviews for all the products in August 2012?
by month: egen avg_price = mean(price)
by month: egen num_review = sum(review_volume)

* (8) Plot sales (and review_volume, and both) against date_id for the first product (product_id=1) across all the time periods in September 2012.
twoway (connected quantity_sold date_id)(connected review_volume date_id) if product_id==1 & month == 9