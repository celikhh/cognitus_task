# Cognitus Task

### Setup
- Run `docker-compose up`


## API

| Route | HTTP Verb	 | POST body	 | Description	 |
| --- | --- | --- | --- |
| /api/data/ | `GET` | Empty | Lists all data. |
| /api/data/ | `POST` | {'label':'foo', 'text':'bar'} | Create a new data. |
| /api/data/:data_id/ | `GET` | Empty | Get a data. |
| /api/data/:data_id/ | `PUT` | {'label':'foo', 'text':'bar'} | Updates data with new info. |
| /api/data/:data_id/ | `PATCH` | {'label':'foo'} or {'text':'bar'} | Updates data with new field. |
| /api/data/:data_id/ | `DELETE` | Empty | Delete a data. |
| /api/train/ | `POST` | Empty | Trains existing data in db. |
| /api/predict/:text | `POST` | Empty | Predict on the given text. |
