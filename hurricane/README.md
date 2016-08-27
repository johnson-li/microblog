Introduction
===

There are so much technology in today's web server development, most of them are beneficial for the web server performance. But to a company, it's important to make out the technology's tradeoff before applying it. This Project aims to measure these tradeoff.

A modern RESTful web sever can be seperated into several layers:
 
- present layer (www)
- businese logic layer (webrpc)
- persisten storage layer (db)
 
Generally, a web server's performance is determined by the implementation of each layer, and the efficiency of their communication.



Architecture
===
As a benchmark system, this project can be seperated into two parts in design

- persistent part
	- `api` each layer should provide a consistent outer interface to provide a fair contest environment
- configurable part
	- `implementation` db provider, etc
	- `communication` different protocal, sync vs async
	- `cache` cache can exist between any 2 layers, but the efficiency and difficulty varies a lot
	
The core of this project is to make use of plenty configurable parts and compare their performance variance. Since there shall be too many configurable parts, I utilize code generation to provide a clean web server to be benchmarked.
