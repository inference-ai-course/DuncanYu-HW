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

## Homework: Vector Search & RAG Pipeline

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

### Data Directory Documentation

#### Overview
The data directory stores various stages of document processing, from raw text extraction to final vector embeddings and search indices.

#### File Structure
```
data/
├── texts.jsonl           # Raw extracted text documents
├── texts_dedup.jsonl     # Deduplicated text documents
├── chunks.jsonl          # Text chunks for embedding
├── faiss_index.faiss     # FAISS vector index
├── faiss_metas.pkl       # Metadata for FAISS index
└── README.md            # This file
```

#### File Descriptions

**`texts.jsonl`**
- **Purpose**: Raw text documents extracted from various sources
- **Format**: JSON Lines format with document metadata
- **Content**: Original documents before any processing
- **Fields**: 
  - `id`: Unique document identifier
  - `title`: Document title
  - `content`: Full document text
  - `source`: Source URL or identifier
  - `metadata`: Additional document information

**`texts_dedup.jsonl`**
- **Purpose**: Deduplicated version of texts.jsonl
- **Format**: Same as texts.jsonl but with duplicates removed
- **Processing**: Uses content hashing to identify and remove duplicate documents
- **Benefits**: Reduces index size and improves search quality

**`chunks.jsonl`**
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

**`faiss_index.faiss`**
- **Purpose**: FAISS vector index for fast similarity search
- **Format**: Binary FAISS index file
- **Content**: Dense vector embeddings of text chunks
- **Index Type**: Typically IVF (Inverted File) or HNSW for efficiency
- **Dimensions**: Usually 384 or 768 depending on embedding model

**`faiss_metas.pkl`**
- **Purpose**: Metadata corresponding to FAISS index entries
- **Format**: Pickle file containing list/dict of metadata
- **Content**: Maps index positions to chunk metadata
- **Usage**: Retrieve original text and metadata from search results

#### Data Processing Pipeline

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

---

## Class Assignment: Document Processing & Vector Search

This week focused on implementing core document processing techniques and vector search capabilities using FAISS for semantic retrieval.

### Document Processing
- **Text Chunking**: Implement intelligent document segmentation strategies
- **Content Preprocessing**: Clean and normalize text for optimal embedding
- **Metadata Extraction**: Preserve document structure and context information

### Vector Search Implementation
- **Embedding Generation**: Create high-quality vector representations
- **FAISS Integration**: Build efficient similarity search infrastructure
- **Index Management**: Optimize storage and retrieval performance

### Query Processing
- **Search Interface**: Develop query processing and ranking systems
- **Retrieval Optimization**: Fine-tune search parameters and algorithms
- **Result Formatting**: Structure search results with relevance scoring

### Implementation Status

#### Document Processing
- [x] Intelligent text chunking algorithms
- [x] Content preprocessing and cleaning
- [x] Metadata preservation and handling

#### Vector Search System
- [x] FAISS vector index creation and setup
- [x] Embedding generation pipeline
- [x] Index optimization and management

#### Query Processing
- [x] Search query processing system
- [x] Retrieval and ranking functionality
- [x] Result formatting and scoring
