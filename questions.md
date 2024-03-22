# Afterward Questions

After completing your implementation, you should include a write up that answers the following
questions:


### 1. Discuss your strategy and decisions implementing the application. Please, consider time complexity, effort cost, technologies used and any other variable that you understand important on your development process.

- About Time Complexity (Big O notation):
  - The base for the solutions, mainly the relationships was thought as to avoid time complexities of O(n²)
    - To do so, we created a strategy that:
      - First load all the related tables O(n)
        - Add all into Python dictionaries (insert operations tends to have a O(1) avg time complexity) 
      - Then mapped the tables: 
        - From the ones with more elements(lets call it 'n')
        - Into the minor ones(lets call it 'm')
        - keeping a O(n) complexity

- About effort cost:
  - How I was far from Django for several years, this gave the most effort to read and remember: syntax, code structures, code conventions, clear startup settings to be easily replicated
  - The idea for a division "MVC" based came quickly and so I implemented a base logic easily
  - After running and with the expected results I begin refactoring mainly to keep the code with good semantic and with clear code structures, with still simple 

- About the technologies:
  - I was far from Django for some time, but I got the citation to it in the challenge description as a hint of what I would end up using in the work, so I went for it
  - I frequently work with python for BI related scripts, jupyter queries and the likes of it, so it was easy to write the pure Python parts
  - I didn't need any extra libs, so I think that in technologies is that

- About other points:
  - I think that I spend a considerable time also thinking about how to present the outputs, with led into some over thinking due to didn't have much clues as how this data will be used

- About tests:
  - I tested it on the run through the API responses, but decided to add a Django `TestCase` just in case
    - It can be run through the command: `./manage.py test`


### 2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?

- If isn't a new relation, just a atomic field:
  - It would only be necessary to add it on the `quorum_app/models.py`
  - if it would show up in the output, we must also add into `quorum_app/render.py`
- If it implies in new relation into the tables
  - It would be necessary to add the necessary mapping into `quorum_app/map_tables.py`

### 3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

- I see two different paths based on the chance
  - If we needed to receive a list and append to the CSV
    - My steps would be:
      - Add a http `PUT` route, that would accept a JSON array
      - This route should append the data to the `data_dir`
      - Everything else should be the same
  - If we needed to receive a list (or set of lists) and work with them on the run
    - My steps would be:
      - Add a http `PUT` route, that would accept the lists
      - Add the lists over a `/temp/:ID` directory and define a ID for this temporary execution
      - Change the `quorum_app/builder.py` so that it could read from the `/temp/:ID` directory
      - Run everything like the current version
      - Clear the `/temp/:ID` directory


### 4. How long did you spend working on the assignment?
- Remembering Django sintax and creating the base app: 2 hours
- Implementing the logic: 1 hours
- Refactoring for semantics and to fit it better into Python conventions: 1 hours
- Additional Documentation and quality steps: 1 hours


## Usage
Then we just need to access the endpoints, there are both the JSON version and html based one
```curl
for JSON
curl http://localhost:8000/legislators/json
curl http://localhost:8000/bills/json

for HTML
curl http://localhost:8000/legislators
curl http://localhost:8000/bills
```

## License

[MIT](https://choosealicense.com/licenses/mit/)