#!/usr/bin/env python
# coding: utf-8

# In[3]:


def calculate_metrics(named_entities_generated, named_entities_source, named_entities_ground_truth):
    """
    Calculate precision-source, precision-target, and recall-target metrics.
    
    Parameters:
    named_entities_generated (set): Named entities in the generated summary.
    named_entities_source (set): Named entities in the source document.
    named_entities_ground_truth (set): Named entities in the ground truth summary.
    
    Returns:
    tuple: precision_source, precision_target, recall_target
    """
    
    # Precision-source
    precision_source = len(named_entities_generated.intersection(named_entities_source)) / len(named_entities_generated) if named_entities_generated else 0
    
    # Precision-target
    precision_target = len(named_entities_generated.intersection(named_entities_ground_truth)) / len(named_entities_generated) if named_entities_generated else 0
    
    # Recall-target
    recall_target = len(named_entities_generated.intersection(named_entities_ground_truth)) / len(named_entities_ground_truth) if named_entities_ground_truth else 0

    return precision_source, precision_target, recall_target

# Example usage
named_entities_generated = {"OpenAI", "San Francisco"}
named_entities_source = {"OpenAI", "San Francisco", "Technology"}
named_entities_ground_truth = {"OpenAI", "San Francisco"}

precision_source, precision_target, recall_target = calculate_metrics(
    named_entities_generated, named_entities_source, named_entities_ground_truth
)

print("Precision-source:", precision_source)
print("Precision-target:", precision_target)
print("Recall-target:", recall_target)


# In[ ]:




