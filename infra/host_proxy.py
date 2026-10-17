"""Forward host-only WSL network ports to loopback lab services."""
import socket, socketserver, threading, select, subprocess
ip=subprocess.check_output(['hostname','-I'],text=True).split()[0]
class Proxy(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            with socket.create_connection(('127.0.0.1',self.server.target),timeout=8) as remote:
                sockets=[self.request,remote]
                while True:
                    ready,_,_=select.select(sockets,[],[],120)
                    if not ready: break
                    for current in ready:
                        data=current.recv(65536)
                        if not data: return
                        (remote if current is self.request else self.request).sendall(data)
        except OSError: pass
class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address=True
    daemon_threads=True
for external,internal in [(18081,8081),(18000,8000)]:
    server=Server((ip,external),Proxy); server.target=internal
    threading.Thread(target=server.serve_forever,daemon=True).start()
    print(f'WSL host-only {ip}:{external} -> 127.0.0.1:{internal}',flush=True)
threading.Event().wait()
