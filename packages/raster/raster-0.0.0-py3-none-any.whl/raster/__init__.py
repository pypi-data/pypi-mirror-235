import numpy as np
from osgeo import gdal, gdal_array


def read_geotiff(file_path):
    '''
    从GeoTIFF文件中读取数据, 返回: data, cols, rows, bands, geotrans, proj

    参数:
        - file_path (str): GeoTIFF文件的路径.

    返回:
        - data (numpy.ndarray): 读取的数据数组,  data.shape = (bands, rows, cols)
        - cols (int): 数据宽度, 列
        - rows (int): 数据高度, 行
        - bands (int): 数据波段数.
        - geotrans (tuple): 仿射变换参数, 元组: (左上角x坐标, 水平分辨率, 旋转参数, 左上角y坐标, 旋转参数, -垂直分辨率)
        - proj (str): 投影信息.
    '''
    try:
        dataset = gdal.Open(file_path)  # 打开GeoTIFF文件
        if dataset is None:
            raise RuntimeError(f"Failed to open GeoTIFF file: {file_path}")

        cols = dataset.RasterXSize  # 获取宽度
        rows = dataset.RasterYSize  # 获取高度
        bands = dataset.RasterCount  # 获取波段数
        data = dataset.ReadAsArray()  # 读取数据
        geotrans = dataset.GetGeoTransform()  # 获取仿射变换参数
        proj = dataset.GetProjection()  # 获取投影信息

        return data, cols, rows, bands, geotrans, proj

    except Exception as e:
        print(f"Error in reading GeoTIFF file: {str(e)}")
        return None, None, None, None, None, None

    finally:
        if dataset is not None:
            dataset = None  # 释放资源



def write_geotiff(data, geotrans, proj, output_path, options=["TILED=YES", "COMPRESS=LZW"]):
    '''
    将数据写入GeoTIFF文件, 输入: data, geotrans, proj, output_path

    参数:
        - data (numpy.ndarray): 要写入的数据数组, data.shape = (bands, rows, cols)
        - geotrans (tuple): 仿射变换参数, 元组: (左上角x坐标, 水平分辨率, 旋转参数, 左上角y坐标, 旋转参数, -垂直分辨率)
        - proj (str): 投影信息.
        - output_path (str): 输出文件的路径.
        - options=["TILED=YES", "COMPRESS=LZW"] 设置选项, 启用切片和LZW压缩
    '''
    try:
        datatype = gdal_array.NumericTypeCodeToGDALTypeCode(data.dtype)  # 获取数据类型代码
        driver = gdal.GetDriverByName("GTiff")  # 获取GTiff驱动程序
        if len(data.shape) == 2:
            data = np.array([data])             # 如果是二维数据，则转换为三维数组
        bands, rows, cols = data.shape       # 获取数据的波段数、高度和宽度
         
        if options is None:
            options = []  # 默认为空列表
        dataset = driver.Create(output_path, cols, rows, bands, datatype, options=options)
        if dataset is None:
            raise RuntimeError("Failed to create output GeoTIFF file.")

        dataset.SetGeoTransform(geotrans)  # 设置仿射变换参数
        dataset.SetProjection(proj)  # 设置投影信息
        for band_index, band_data in enumerate(data, start=1):
            dataset.GetRasterBand(band_index).WriteArray(band_data)  # 写入数据数组

        dataset.FlushCache()  # 刷新缓存

    except Exception as e:
        print(f"Error in writing GeoTIFF file: {str(e)}")

    finally:
        if dataset is not None:
            dataset = None  # 关闭文件
