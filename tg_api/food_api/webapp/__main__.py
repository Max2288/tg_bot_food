import uvicorn

if __name__ == '__main__':
    uvicorn.run('webapp.main:create_app', host='0.0.0.0', port=1025, factory=True, reload=True)