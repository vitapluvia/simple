FROM angr/angr
RUN mkdir /home/angr/simple
ADD *simple* /home/angr/simple/
RUN chown -R angr:angr /home/angr/simple
