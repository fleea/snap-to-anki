RAMBLE WARNING

Kind of diary of this project, you can mostly ignore it.
But if you want to get a sneakpeek on challenges and design decisions, you are very welcome.

10 March 2025
- Considering LayoutLM for Layout Analysis
  - For mixed content, it might be beneficial (image + vocab table + text)
  - However, it seems the segment is not working well (too fine grained)
  - Parking it for now, but will be back when we want to increase accuracy
- PROMPT Design
  - content_analysis
    - Get the language
    - Think about what's inside the image
    - Is it a dictionary? Then probably user just want a simple set of questions answer to remember vocabularies.
    - Is it containing images? Do you think it's a decorative image or something important to be remembered?
    - Extract relevant information from the layout
    - Check if answer is included in the image, if yes, use that answer, if not generate answer with "AI-generated" tag
    - Add user comment in the input so user can add custom processing instructions
    - IMPORTANT: The model should be able to handle large image (large token window), ability to extract data
  - flashcard_writer
    - Analyze which anki type is suitable for this image
    - Do not use structured output (return csv directly)

12 March 2025
- Unable to process base64_encoding without hitting token limit
- Decided to upload the image publicly then add the url to open_ai system text
- CONS: Image will be (temporarily) exposed in public folder

13 March 2025
- Contemplating if I should use structured_output JSON Schema and then processing it to csv in flashcard_writer
  - PRO: Probably type safe and increasing accuracy
  - CONS: Cost (JSON is larger), latency (need to have another node/parser to process the output)
- Apparently, claude is quite good is being the judge of a prompt
- Accuracy for mixed content can be better
  - Add LLM as a judge for the last loop?
- Built Openrouter Integration to check multiple other models. Make it generic so Langchain original init_chat_model can still be used
- Google just dropped Gemma3, let's try to use it
- Structured output with Gemma3 is still not ideal

14 March 2025
- Added specialized prompts for each segment type to add accuracy
- Decided to add all specialized prompts to the single writer prompt
- Other options is to add another llm call (and extra node) per segment, but I think it will be too much
- Contemplating if I should filter out generative segment in the node or asking llm to filter it out (in case upstream error)