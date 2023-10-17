from logclshelper import LogClsHelper
from pysparkhelper import PySparkHelper
from pysparkhdfshelper import PySparkHdfsHelper
from pysparkparquethelper import PySparkParquetHelper

class PySparkParquetTable(LogClsHelper):
    
    def init(self, paths):
        self.paths = paths
        self._files = None
        
    def files(self):
        self.logger().debug('#beg# files')
        
        if(self._files is None):            
            self._files = PySparkParquetHelper.get_sorted_files_by_last_part_value_from_paths(self.paths)
            
        self.logger().debug('#end# files')
        
        return self._files
        
    def df_from_file(self, file):
        return PySparkParquetHelper.read_parquet_from_file(file)
    
    def df_from_files_chunk(self, files_chunk):
        return PySparkParquetHelper.read_parquet_from_files_chunk(files_chunk)
    
    def yield_dfs_from_files_chunk(self, files_chunk):
        for file in files_chunk:
            yield self.df_from_file(file)
            
    def df_from_files_chunk_by_union_dfs(self, files_chunk):
        return PySparkParquetHelper.union_dfs_by_name(self.yield_dfs_from_files_chunk(files_chunk))

