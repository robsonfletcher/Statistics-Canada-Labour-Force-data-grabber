def labour_force(pid, vectors, periods):
    """
    Labour Force data graber (in fact.... probably works with all Stats Canada tables)
    Provide table id (8 charachters), desired vectors and number of periods to get a handy tidy data dataframe.
    Note: one each vector sends three POST requests to Stats Canada, so ideally to be used for smaller one-off data requests.
    
    pid: int, the 8-digit table ID
    vectors: list of ints,
    periods: int, number of desired reference periods
    """
    lists = []

    for vector in vectors:

        # get dimension option values
        rr = requests.post(url='https://www150.statcan.gc.ca/t1/wds/rest/getSeriesInfoFromVector',
                         data=f'[{{"vectorId":{str(vector)}}}]',
                         headers={'Content-Type': 'application/json'})

        dim_values = json.loads(rr.text)[0]['object']['SeriesTitleEn'].split(';')

        # get available dimensions
        r = requests.post(url='https://www150.statcan.gc.ca/t1/wds/rest/getCubeMetadata',
                         data=f'[{{"productId":{str(pid)}}}]',
                         headers={'Content-Type': 'application/json'})

        dimensions = [json.loads(r.text)[0]['object']['dimension'][i]['dimensionNameEn'] for i in list(range(0,len(dim_values)))]
        dimensions = dimensions + ['Date', 'Value']

        # get values and ref date
        rrr = requests.post(url='https://www150.statcan.gc.ca/t1/wds/rest/getDataFromVectorsAndLatestNPeriods',
                         data=f'[{{"vectorId":{str(vector)}, "latestN":{periods}}}]',
                         headers={'Content-Type': 'application/json'})

        for i in list(range(0, periods)):
            vals = [json.loads(rrr.text)[0]['object']['vectorDataPoint'][i]['refPer']] + [json.loads(rrr.text)[0]['object']['vectorDataPoint'][i]['value']]
            rows = dim_values + vals

            lists.append(rows)
            
            df = pd.DataFrame(lists, columns=dimensions)
            df['Date'] = pd.to_datetime(df['Date'])

    return df
