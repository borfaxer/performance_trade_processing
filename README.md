
Hello!

I created a Docker container so it would be easy for someone (with Docker)
to create an envronment where this code works. I used the following 
commands in the same directory as the Dockerfile and Python script to create 
a Docker container and open a bash prompt in it:

docker build -t performance_trade_processing .

docker run -it -w /app -v "$(pwd):/app" --rm --name ws performance_trade_processing

What you will need:
- Docker to create the container OR Pypy installed wherever you run this
- The binary that produces trades

In a unix-based terminal, from the same directory as the binary and 
the Python code you should be able to run:

./stdoutinator_amd64_linux.bin | ./meanie.py

I measured performance by prepending the time command.

Baseline performance in a Docker container on my laptop was ~15 seconds just
to output the trades:

time ./stdoutinator_amd64_linux.bin > /dev/null

The actual performance testing with my code used this command:

time ./stdoutinator_amd64_linux.bin | ./meanie.py

My first Python code took ~90 seconds to run. Streamlining the imports and 
optimizing out the two dot (.) operators in the execution loop improved it by 
11% to ~80 seconds. Installing Pypy and converting the script to use that
instead of the standard Python interpreter cut execution time to 19-22 seconds.
Given that this is within 50% of the baseline performance, I'm satisfied enough
for this exercise. A commercial service running constantly every day where 
performance is critical would obviously deserve even more performance gains, 
but this would probably require switching to a more inherently performant 
language.

-- Jake Sorensen

