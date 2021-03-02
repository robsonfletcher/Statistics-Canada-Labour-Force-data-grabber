# Statistics-Canada-Labour-Force-data-grabber
Easy function for quickly getting tidy data of any Labour Force data table.
Script should also work on any Table within Statistics Canada's data repositories.

Note: this is a terribly inefficient way for gathering large datasets as each desired vector
send three POST requests to Stast Canada. So.... this is a work in progress. But was done in haste
to get a project off the ground quickly.

## How the function works

1. Determine the Table ID for the CANSIM table that contains your desired data.
2. Get list of all the desired timeseries vectors.
3. Determine how many date_reference periods you want.

The function will retrieve the data values, dimensions values and dimensions (to be set as the header) and then output a dataframe in tidy data form.

## About isolating data using vectors:

> What is a vector?
> > Unique variable length reference code time-series identifier, consisting of the letter 'V', followed by up to 10 digits. (i.e. V1234567890, V1, etc.)

## More
Many of the time-series data available from Statistics Canada have individual vector codes. These vector codes follow a naming format of a lower-case “v” and an identifying numbers. Time-series tables will often bundle many series together, resulting in large and sometimes unwieldy files. Many users of Canadian statistical data, who are often concerned with specific time series such as the CPI or international arrivals, will typically know the exact series they need. For this reason, the cansim package also provides two functions to make it easier to retrieve individual vectors: get_cansim_vector() and get_cansim_vector_for_latest_periods().
> (source for above paragraph: https://mountainmath.github.io/cansim/articles/retrieving_cansim_vectors.html)
