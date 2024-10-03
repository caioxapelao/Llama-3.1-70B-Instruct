import nodriver as uc
import asyncio

async def main(prompt, wtime):
    driver = await uc.start()
    tab = await driver.get('https://huggingface.co/chat/')

    txtarea = await tab.select('textarea.scrollbar-custom')
    await txtarea.send_keys(prompt)
    submitbtn = await tab.select('.mx-1')
    await submitbtn.click()
    await tab.sleep(wtime)
    results = await tab.select('.prose')
    print(results.text)

uc.loop().run_until_complete(main("Hello! How are you doing?", 5))
    
