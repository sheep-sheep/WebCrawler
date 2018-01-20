# WebCrawler

1. Created a basic Spider to find specific target based on the pattern
2. Expaned the Spider to do a BFS search for similiar attrs
3. Created an enumerated script based on the url pattern i have found

4. Apply multiprocessing to the script since i think it's an I/O bound task

5. Implemented a @timeit decorator and make it pickleable for multiprocessing

6. CPU analysis when querying 50 url and download images on a 4-core CPU
The up-down looks reall nice and has a harmony in it!
![WebCrawler](images/4 Cores.png "Screenshot of my taskmanager")
