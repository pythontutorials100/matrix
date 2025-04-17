Hello everyone. 
I'm Shatad Purohit. 
Today, I'll be discussing data integration for connected products, specifically through the lens of our recent PW-USAF Pilot project. 
This effort focused on creating an Inspection Digital Twin with the goal of significantly Improving Repair Process Efficiency. 
We'll walk through the challenges and the knowledge-based solution we've developed.

-----


Ensuring the safety and readiness of our advanced engines depends critically on how we perform inspection and repair of parts like airfoils. 
We have excellent tools generating valuable data, but the way this data currently exists presents a significant challenge – and a clear opportunity for improvement.
Let's look at the current situation, as outlined on the slide. We have sophisticated inspection tools that scan airfoils for defects. 
These tools generate detailed measurements – like defect length, depth, and distance from specific datum points – typically producing numerical data in a tabular format, like a spreadsheet or database table.
Separately, we often rely on localization rules, frequently written as plain text in documents, to help interpret that scan data and correctly pinpoint defect locations on the part.
And of course, we have the essential 3D models of the airfoils themselves, usually as standard STL files.
Furthermore, Pratt & Whitney utilizes cutting-edge FEA simulations. These simulations are crucial for determining the optimal repair procedures for identified defects. They calculate precise parameters like the required blend shape, fillet radius for edges, or blend length, considering various defect types and repair strategies. 
However, this vital repair information typically comes out in yet another distinct format – JSON files.

So, here's the core challenge: All these valuable pieces of information – the tabular scan data, the text rules, the 3D models, the JSON repair specifications – essentially exist separately. They are scattered, often residing in different systems or locations, and crucially, in different formats. As the slide highlights, the data is heterogeneous and siloed.

Currently, there is no established, automated way to connect these dots. There's no system linking a specific defect identified in the tabular scan data directly to its unique, corresponding repair parameters sitting in a JSON file, or easily relating either of those back to the text rules and the 3D model.
This lack of integration forces engineers into time-consuming manual efforts just to connect the necessary data for analysis or repair.
This difficulty in bringing the data together leads to several key impacts:"
•	First, it inherently slows down analysis and potential repair decisions. Time would be spent assembling data instead of acting on it.
•	Second, it prevents a truly holistic view. Without integration, you can't easily see the complete story of a defect and its specific, calculated repair recommendation in one place. This hinders deeper understanding and makes advanced analysis across many parts very difficult.
•	And third, looking strategically, this fragmented data landscape fundamentally blocks the path towards standardized, machine-readable data sharing between partners like Pratt & Whitney and the Air Force. Achieving that future state of efficient collaboration requires integrated, structured data, which we don't have today for this process.

In essence, we have valuable islands of data, but no automated bridges connecting them. This hinders efficiency and insight today and limits our potential for smarter and more integrated operations tomorrow. Addressing this integration challenge is the core focus of our Knowledge Graph pilot.

-------------

So, how did we bridge those data islands and transform the process? As the slide title indicates, we focused on creating an Inspection Digital Twin, powered by a Knowledge Graph."
Our core solution, as you see listed on the left, was to automatically connect that siloed data. We did this by building a formal ontology-based Knowledge Graph.

Think of this graph structure, shown here, as the 'digital brain'. We used an ontology – a smart data model – to explicitly define aspects related to the airfoils, defects, measurements, the different FEA repair parameters, the text rules, and importantly, how they all relate, we defined that also. 
To ensure this aligns with broader enterprise efforts, we reused modeling patterns from the RTX Enterprise Ontology (REO).

This structured graph allows us to then query and reason over the connected data using standard methods like SPARQL, as illustrated here. This enables us to ask complex questions that span across the different original data sources.
And it unlocks the potential for advanced analysis, like spotting trends or correlations across datasets.

But the most critical output is providing that unified view for the user. If you look at the demonstration interface, you see exactly what this enables."
We load the 3D airfoil model. Then, using those SPARQL queries against the Knowledge Graph, to pull all the relevant, linked information for a selected defect.
We can mark the defect location directly on the 3D model. And most importantly, look at the tables: We have the defect information from the inspection scan data and corresponding repair information – like fillet radius and blend length – pulled from the FEA simulation results. The previously separate pieces are now presented together, in context."
(Transition to Value - Directly link the output to the benefits)
"This integrated output delivers significant value, as summarized on the left:"
•	"It provides easily consumable information directly to the operator or engineer in that unified view we just saw."
•	"This leads to faster and truly integrated insights, drastically reducing the time needed to manually assemble data for decisions."
•	"Because the relationships are explicitly defined in the ontology, it drives improved accuracy and consistency compared to manual interpretation."
•	"Critically, representing the data this way establishes a foundation for standardization. We now have a potential machine-readable description for airfoil distress and repair, paving the way for future interoperability."
(Highlight Validation and Knowledge Transfer)
•	"The success and value of this approach were validated through positive feedback from both PW and the Air Force stakeholders during joint presentations, and importantly, this has secured approval for the next phase of the project."
•	"Finally, a key part of this pilot was capability building. We successfully transferred know-how to Pratt & Whitney, training 28 individuals across five detailed sessions, providing them with tutorials, the actual use case data, and supporting files to ensure they can leverage and build upon this work.



