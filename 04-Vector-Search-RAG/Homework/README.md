# Week 4 – Vector Search & RAG Pipeline

This week focused on building a complete RAG (Retrieval-Augmented Generation) pipeline using vector search with FAISS and comprehensive document processing.

## Tasks

### Document Processing Pipeline
- **Web Scraping**: Automated ArXiv paper collection and metadata extraction
- **Text Extraction**: Clean text extraction from various document formats
- **Content Cleaning**: Preprocessing and normalization of extracted text

### Vector Search Implementation
- **Text Chunking**: Intelligent document segmentation for optimal retrieval
- **Embedding Generation**: Vector representations using sentence transformers
- **FAISS Indexing**: High-performance vector similarity search implementation

### Web Interface Development
- **FastAPI Backend**: RESTful API for search and pipeline management
- **Search Functionality**: Semantic search with relevance ranking
- **Pipeline Orchestration**: Automated processing workflow management

## Status

- [x] **Document Processing Pipeline**
    - [x] ArXiv paper scraping and collection
    - [x] Text extraction and cleaning algorithms
    - [x] Content preprocessing and normalization

- [x] **Vector Search System**
    - [x] Intelligent text chunking implementation
    - [x] Sentence transformer embedding generation
    - [x] FAISS vector index creation and management

- [x] **Web Interface & API**
    - [x] FastAPI backend development
    - [x] Search endpoint with ranking algorithms
    - [x] Pipeline management and orchestration

---

## Data Directory Documentation

### Overview

The data directory stores various stages of document processing, from raw text extraction to final vector embeddings and search indices.

### File Structure

```
data/
├── texts.jsonl           # Raw extracted text documents
├── texts_dedup.jsonl     # Deduplicated text documents
├── chunks.jsonl          # Text chunks for embedding
├── faiss_index.faiss     # FAISS vector index
├── faiss_metas.pkl       # Metadata for FAISS index
└── README.md            # This file
```

### File Descriptions

#### `texts.jsonl`
- **Purpose**: Raw text documents extracted from various sources
- **Format**: JSON Lines format with document metadata
- **Content**: Original documents before any processing
- **Fields**: 
  - `id`: Unique document identifier
  - `title`: Document title
  - `content`: Full document text
  - `source`: Source URL or identifier
  - `metadata`: Additional document information

#### `texts_dedup.jsonl`
- **Purpose**: Deduplicated version of texts.jsonl
- **Format**: Same as texts.jsonl but with duplicates removed
- **Processing**: Uses content hashing to identify and remove duplicate documents
- **Benefits**: Reduces index size and improves search quality

#### `chunks.jsonl`
- **Purpose**: Text chunks optimized for embedding and retrieval
- **Format**: JSON Lines with chunk-specific metadata
- **Processing**: Documents split into semantically coherent chunks
- **Fields**:
  - `chunk_id`: Unique chunk identifier
  - `doc_id`: Parent document ID
  - `text`: Chunk content
  - `start_pos`: Starting position in original document
  - `end_pos`: Ending position in original document
  - `embedding`: Vector embedding (if pre-computed)

#### `faiss_index.faiss`
- **Purpose**: FAISS vector index for fast similarity search
- **Format**: Binary FAISS index file
- **Content**: Dense vector embeddings of text chunks
- **Index Type**: Typically IVF (Inverted File) or HNSW for efficiency
- **Dimensions**: Usually 384 or 768 depending on embedding model

#### `faiss_metas.pkl`
- **Purpose**: Metadata corresponding to FAISS index entries
- **Format**: Pickle file containing list/dict of metadata
- **Content**: Maps index positions to chunk metadata
- **Usage**: Retrieve original text and metadata from search results

### Data Processing Pipeline

1. **Text Extraction** → `texts.jsonl`
   - Extract text from PDFs, web pages, documents
   - Store with metadata and source information

2. **Deduplication** → `texts_dedup.jsonl`
   - Remove duplicate documents using content hashing
   - Preserve unique documents only

3. **Chunking** → `chunks.jsonl`
   - Split documents into optimal chunk sizes
   - Maintain semantic coherence
   - Add positional metadata

4. **Embedding & Indexing** → `faiss_index.faiss` + `faiss_metas.pkl`
   - Generate vector embeddings for chunks
   - Build FAISS index for fast retrieval
   - Store metadata for result mapping

### Data Statistics

Typical dataset characteristics:
- **Documents**: 1,000-10,000 papers/articles
- **Chunks**: 10,000-100,000 text segments
- **Index Size**: 50MB-500MB depending on corpus size
- **Embedding Model**: sentence-transformers/all-MiniLM-L6-v2 or similar

### Data Usage Examples

#### Loading Data
```python
import json

# Load chunks
chunks = []
with open('data/chunks.jsonl', 'r') as f:
    for line in f:
        chunks.append(json.loads(line))

# Load FAISS index
import faiss
import pickle

index = faiss.read_index('data/faiss_index.faiss')
with open('data/faiss_metas.pkl', 'rb') as f:
    metadata = pickle.load(f)
```

#### Searching
```python
# Perform similarity search
query_vector = model.encode(["your query here"])
scores, indices = index.search(query_vector, k=5)

# Retrieve metadata
results = [metadata[idx] for idx in indices[0]]
```

### Data Maintenance

#### Updating the Index
1. Add new documents to `texts.jsonl`
2. Run deduplication process
3. Re-chunk documents
4. Rebuild FAISS index
5. Update metadata file

#### Index Optimization
- **Rebalancing**: Periodically rebuild index for optimal performance
- **Pruning**: Remove outdated or low-quality documents
- **Compression**: Use quantization for smaller index size

### Performance Considerations

- **Index Type**: Choose appropriate FAISS index based on dataset size
- **Chunk Size**: Balance between context and granularity (typically 200-500 tokens)
- **Embedding Model**: Trade-off between quality and speed
- **Memory Usage**: Monitor RAM usage for large indices
