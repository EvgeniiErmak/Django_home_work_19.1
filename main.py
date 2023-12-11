from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Открываем файл index.html и читаем его содержимое
            with open(os.path.join(os.path.dirname(__file__), 'index.html'), 'rb') as file:
                content = file.read()

            # Отправляем HTTP-заголовки
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Отправляем содержимое файла index.html
            self.wfile.write(content)
        except FileNotFoundError:
            # Если файл не найден, возвращаем ошибку 404
            self.send_error(404, 'File Not Found: index.html')


if __name__ == '__main__':
    # Задаем хост и порт
    host = 'localhost'
    port = 8080

    # Создаем HTTP-сервер и запускаем его
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f'Starting server on http://{host}:{port}')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        # При нажатии Ctrl+C завершаем сервер
        pass
    httpd.server_close()
    print('Server stopped')
